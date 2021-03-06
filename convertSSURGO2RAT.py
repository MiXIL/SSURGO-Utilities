#! /usr/bin/env python

#######################################
# convertSSURGO2RAT.py
# A script for converting selected attributes for
# SSURGO soil data to a raster attribute table
# and optionally a standard raster (one band
# per attribute)
# 
# Requires:
# rios (https://bitbucket.org/chchrsc/rios/overview)
# RSGISLib (http://www.rsgislib.org/doku.php)
# kealib (https://bitbucket.org/chchrsc/kealib/overview)
# and dependencies for these libraries
#
# Dan Clewley (daniel.clewley@gmail.com)
# 09/10/2012
#
# Function to link tables adapted from FORTRAN code
# provide by Jane Whitcomb
#
# Updated 27/04/2014 (Dan Clewley)
# - Use arparse to read in parameters
# - Can input multiple column names
# - Optionally export each column to a raster
#######################################


import os, sys, csv, glob
import argparse
import numpy
import subprocess
import rsgislib
from rios import rat
from rsgislib import rastergis
from rsgislib import vectorutils
sys.path.append(os.sys.path[0])
from ssurgofields import SSURGO_CHorizion

def getFileExtension(gdalFormat):
    """
    A function to get the extension for a given file format 
    (NOTE, currently only KEA, GTIFF, HFA, PCI and ENVI are supported).
    """
    ext = None
    if gdalFormat.lower() == "kea":
        ext = "kea"
    elif gdalFormat.lower() == "hfa":
        ext = "img"
    else:
        raise Exception("The extension for '{}' is unknown or the format does not support Raster Attribute Tables".format(gdalFormat))
    return ext

parser = argparse.ArgumentParser(description='''Create Raster Atttribute Table (RAT) in KEA format
from SSURGO data. If the KEA file exists, new attributes are appended to the RAT.''')
parser.add_argument("--indir", type=str, default=None, help="Don't calculate stats for output slope image.")
parser.add_argument("--colname", type=str, action='append', help="Column names to export.", required=False)
parser.add_argument("--raster", action='store_true', default=False, help="Export raster image for selected column (Default: False).")
parser.add_argument("--outRes", type=float, default=0.0002777777777777778, help="Output resolution (Default: 1 arcsec)")
parser.add_argument("--printcols", action='store_true', default=False, help="Print available column names")
parser.add_argument("--outformat", type=str, default="KEA", help="GDAL name for output raster format (Default: KEA)")
args = parser.parse_args() 

sf = SSURGO_CHorizion()

if args.printcols:
    sf.printNames()
    sys.exit()
elif args.indir is None or args.colname is None:
    print('ERROR: Must provide input directory and at least one colum name')
    parser.print_help()
    sys.exit()

inDIRName = os.path.abspath(args.indir)
outColName = sys.argv[2] 
outXRes = str(args.outRes)
outYRes = '-' + outXRes

outFormat = args.outformat
try:
    outExt = getFileExtension(outFormat)
except Exception as err:
    print('ERROR:')
    print(err)
    sys.exit()

# Import dictionary of values
cHorizonFields = sf.getCHorizonDict()


# CREATE RASTER ATTRIBUTE TABLE
inSpatialDIR = os.path.join(inDIRName, 'spatial')
inSHPName = glob.glob(inSpatialDIR + '/*soilmu_a_*.shp')[0]
inSHPFile = os.path.join(inSpatialDIR, inSHPName)
 
outKEAFile = inSHPFile.replace('.shp', '_raster.' + outExt)

# Check if KEA file exists or needs creating - assume if it exists it has the attribute table already
if os.path.exists(outKEAFile) == False: 
    # Rasterize polygon using gdal
    print('Creating raster')
    rasterizeCommand = ['gdal_rasterize', '-of', outFormat, 
                        '-ot', 'UInt32',
                        '-tr', outXRes, outYRes,
                        '-a', 'MUKEY',
                        inSHPFile, outKEAFile]
    subprocess.call(rasterizeCommand)

    # Convert to RAT and add entry 'mukey' using RSGISLib
    rastergis.populateStats(outKEAFile, True, True)
    stats2Calc = [rastergis.BandAttStats(band=1, minField='mukey')]
    rastergis.populateRATWithStats(outKEAFile, outKEAFile, stats2Calc)

# Iterate through column names
for outColName in args.colname:
    # Set up name for standard raster file
    outRasterImage = inSHPFile.replace('.shp', '_raster_' + outColName + '.' + outExt)

    # Get field from dictionary
    outColNum = cHorizonFields[outColName.strip()]

    # JOIN ATTRIBUTES FROM TEXT FILE
    print('Adding ' + outColName + ' (column ' + str(outColNum) + ') to RAT')
    # Open SSURGO text files
    componentFileName = os.path.join(inDIRName, 'tabular', 'comp.txt')
    chorizonFileName = os.path.join(inDIRName, 'tabular', 'chorizon.txt')

    componentFile = open(componentFileName, 'rU')
    chorizonFile = open(chorizonFileName,'rU')

    componentTxt = csv.reader(componentFile, delimiter='|')
    chorizonTxt = csv.reader(chorizonFile, delimiter='|')

    # Get mukey column from input file
    mukeyCol = rat.readColumn(outKEAFile, 'mukey')
 
    # Set up blank columns for output (one for each layer)
    outColH1 = numpy.zeros_like(mukeyCol)
    outColH2 = numpy.zeros_like(mukeyCol) 
    outColH3 = numpy.zeros_like(mukeyCol) 
    outColH4 = numpy.zeros_like(mukeyCol)
    outColH5 = numpy.zeros_like(mukeyCol)
    outColH6 = numpy.zeros_like(mukeyCol)
    
    # Set columns for mukey and cokey in componentTxt
    compMUKEYCol = 107
    compCOKEYCol = 108
    
    chorizonCOKEYCol = 169
    chorizonHZNAMECol = 0

    for i in range(mukeyCol.shape[0]):
        mukey = mukeyCol[i]
        if mukey > 0:
            componentFile.seek(0) # Reset position in CSV file
            for component in componentTxt:
                if int(component[compMUKEYCol]) == int(mukey):
                    cokey = component[compCOKEYCol]
                    chorizonFile.seek(0) # Reset position in CSV file
                    for chorizon in chorizonTxt:
                        if (chorizon[chorizonCOKEYCol] == cokey) and (chorizon[outColNum] != ''):
                            if chorizon[chorizonHZNAMECol] == 'H1':
                                outColH1[i] = chorizon[outColNum]
                            elif chorizon[chorizonHZNAMECol] == 'H2':
                                outColH2[i] = chorizon[outColNum]
                            elif chorizon[chorizonHZNAMECol] == 'H3':
                                outColH3[i] = chorizon[outColNum]
                            elif chorizon[chorizonHZNAMECol] == 'H4':
                                outColH4[i] = chorizon[outColNum]
                            elif chorizon[chorizonHZNAMECol] == 'H5':
                                outColH5[i] = chorizon[outColNum]
                            elif chorizon[chorizonHZNAMECol] == 'H6':
                                outColH6[i] = chorizon[outColNum]
                    break
    
    rat.writeColumn(outKEAFile, outColName + '_H1', outColH1)
    rat.writeColumn(outKEAFile, outColName + '_H2', outColH2)
    rat.writeColumn(outKEAFile, outColName + '_H3', outColH3)
    rat.writeColumn(outKEAFile, outColName + '_H4', outColH4)
    rat.writeColumn(outKEAFile, outColName + '_H5', outColH5)
    rat.writeColumn(outKEAFile, outColName + '_H6', outColH6)

    if args.raster:
        # Create a list of out column names (attribute and height)
        outColNamesList = ['{}_H{}'.format(outColName, i) for i in range(1, 7)]
        rastergis.exportCols2GDALImage(outKEAFile, outRasterImage,
                                       outFormat, rsgislib.TYPE_32FLOAT,
                                       outColNamesList)
        print('Saved raster to: {}'.format(outRasterImage))

