SSURGO Utilities
=================

* convertSSURGO2RAT.py

Convert downloaded SSURGO spatial and tabular data to a Raster Attribute Table (RAT).
Can optionally export as a separate raster for each column.

Requires:
* GDAL
* RIOS (https://bitbucket.org/chchrsc/rios/)
* RSGISLib (http://www.rsgislib.org/)


Example Usage:

    python convertSSURGO2RAT.py --indir CA669 --colname claytotal_ --raster --outformat HFA

To list all available columns use:

    python convertSSURGO2RAT.py --printcols
