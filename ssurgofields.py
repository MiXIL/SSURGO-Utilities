
class SSURGO_CHorizion (object):

    def __init__(self):
        self.cHorizonDict = self.setCHorizonDict()

    def getCHorizonDict(self):
        return self.cHorizonDict

    def setCHorizonDict(self):
        cHorizonDict = {}
        cHorizonDict['hzname'] = 0
        cHorizonDict['desgndisc'] = 1
        cHorizonDict['desgnmaste'] = 2
        cHorizonDict['desgnmas_1'] = 3
        cHorizonDict['desgnvert'] = 4
        cHorizonDict['hzdept_l'] = 5
        cHorizonDict['hzdept_r'] = 6
        cHorizonDict['hzdept_h'] = 7
        cHorizonDict['hzdepb_l'] = 8
        cHorizonDict['hzdepb_r'] = 9
        cHorizonDict['hzdepb_h'] = 10
        cHorizonDict['hzthk_l'] = 11
        cHorizonDict['hzthk_r'] = 12
        cHorizonDict['hzthk_h'] = 13
        cHorizonDict['fraggt10_l'] = 14
        cHorizonDict['fraggt10_r'] = 15
        cHorizonDict['fraggt10_h'] = 16
        cHorizonDict['frag3to10_'] = 17
        cHorizonDict['frag3to101'] = 18
        cHorizonDict['frag3to1_1'] = 19
        cHorizonDict['sieveno4_l'] = 20
        cHorizonDict['sieveno4_r'] = 21
        cHorizonDict['sieveno4_h'] = 22
        cHorizonDict['sieveno10_'] = 23
        cHorizonDict['sieveno101'] = 24
        cHorizonDict['sieveno1_1'] = 25
        cHorizonDict['sieveno40_'] = 26
        cHorizonDict['sieveno401'] = 27
        cHorizonDict['sieveno4_1'] = 28
        cHorizonDict['sieveno200'] = 29
        cHorizonDict['sieveno2_1'] = 30
        cHorizonDict['sieveno2_2'] = 31
        cHorizonDict['sandtotal_'] = 32
        cHorizonDict['sandtotal1'] = 33
        cHorizonDict['sandtota_1'] = 34
        cHorizonDict['sandvc_l'] = 35
        cHorizonDict['sandvc_r'] = 36
        cHorizonDict['sandvc_h'] = 37
        cHorizonDict['sandco_l'] = 38
        cHorizonDict['sandco_r'] = 39
        cHorizonDict['sandco_h'] = 40
        cHorizonDict['sandmed_l'] = 41
        cHorizonDict['sandmed_r'] = 42
        cHorizonDict['sandmed_h'] = 43
        cHorizonDict['sandfine_l'] = 44
        cHorizonDict['sandfine_r'] = 45
        cHorizonDict['sandfine_h'] = 46
        cHorizonDict['sandvf_l'] = 47
        cHorizonDict['sandvf_r'] = 48
        cHorizonDict['sandvf_h'] = 49
        cHorizonDict['silttotal_'] = 50
        cHorizonDict['silttotal1'] = 51
        cHorizonDict['silttota_1'] = 52
        cHorizonDict['siltco_l'] = 53
        cHorizonDict['siltco_r'] = 54
        cHorizonDict['siltco_h'] = 55
        cHorizonDict['siltfine_l'] = 56
        cHorizonDict['siltfine_r'] = 57
        cHorizonDict['siltfine_h'] = 58
        cHorizonDict['claytotal_'] = 59
        cHorizonDict['claytotal1'] = 60
        cHorizonDict['claytota_1'] = 61
        cHorizonDict['claysizedc'] = 62
        cHorizonDict['claysize_1'] = 63
        cHorizonDict['claysize_2'] = 64
        cHorizonDict['om_l'] = 65
        cHorizonDict['om_r'] = 66
        cHorizonDict['om_h'] = 67
        cHorizonDict['dbtenthbar'] = 68
        cHorizonDict['dbtenthb_1'] = 69
        cHorizonDict['dbtenthb_2'] = 70
        cHorizonDict['dbthirdbar'] = 71
        cHorizonDict['dbthirdb_1'] = 72
        cHorizonDict['dbthirdb_2'] = 73
        cHorizonDict['dbfifteenb'] = 74
        cHorizonDict['dbfiftee_1'] = 75
        cHorizonDict['dbfiftee_2'] = 76
        cHorizonDict['dbovendry_'] = 77
        cHorizonDict['dbovendry1'] = 78
        cHorizonDict['dbovendr_1'] = 79
        cHorizonDict['partdensit'] = 80
        cHorizonDict['ksat_l'] = 81
        cHorizonDict['ksat_r'] = 82
        cHorizonDict['ksat_h'] = 83
        cHorizonDict['awc_l'] = 84
        cHorizonDict['awc_r'] = 85
        cHorizonDict['awc_h'] = 86
        cHorizonDict['wtenthbar_'] = 87
        cHorizonDict['wtenthbar1'] = 88
        cHorizonDict['wtenthba_1'] = 89
        cHorizonDict['wthirdbar_'] = 90
        cHorizonDict['wthirdbar1'] = 91
        cHorizonDict['wthirdba_1'] = 92
        cHorizonDict['wfifteenba'] = 93
        cHorizonDict['wfifteen_1'] = 94
        cHorizonDict['wfifteen_2'] = 95
        cHorizonDict['wsatiated_'] = 96
        cHorizonDict['wsatiated1'] = 97
        cHorizonDict['wsatiate_1'] = 98
        cHorizonDict['lep_l'] = 99
        cHorizonDict['lep_r'] = 100
        cHorizonDict['lep_h'] = 101
        cHorizonDict['ll_l'] = 102
        cHorizonDict['ll_r'] = 103
        cHorizonDict['ll_h'] = 104
        cHorizonDict['pi_l'] = 105
        cHorizonDict['pi_r'] = 106
        cHorizonDict['pi_h'] = 107
        cHorizonDict['aashind_l'] = 108
        cHorizonDict['aashind_r'] = 109
        cHorizonDict['aashind_h'] = 110
        cHorizonDict['kwfact'] = 111
        cHorizonDict['kffact'] = 112
        cHorizonDict['caco3_l'] = 113
        cHorizonDict['caco3_r'] = 114
        cHorizonDict['caco3_h'] = 115
        cHorizonDict['gypsum_l'] = 116
        cHorizonDict['gypsum_r'] = 117
        cHorizonDict['gypsum_h'] = 118
        cHorizonDict['sar_l'] = 119
        cHorizonDict['sar_r'] = 120
        cHorizonDict['sar_h'] = 121
        cHorizonDict['ec_l'] = 122
        cHorizonDict['ec_r'] = 123
        cHorizonDict['ec_h'] = 124
        cHorizonDict['cec7_l'] = 125
        cHorizonDict['cec7_r'] = 126
        cHorizonDict['cec7_h'] = 127
        cHorizonDict['ecec_l'] = 128
        cHorizonDict['ecec_r'] = 129
        cHorizonDict['ecec_h'] = 130
        cHorizonDict['sumbases_l'] = 131
        cHorizonDict['sumbases_r'] = 132
        cHorizonDict['sumbases_h'] = 133
        cHorizonDict['ph1to1h2o_'] = 134
        cHorizonDict['ph1to1h2o1'] = 135
        cHorizonDict['ph1to1h2_1'] = 136
        cHorizonDict['ph01mcacl2'] = 137
        cHorizonDict['ph01mcac_1'] = 138
        cHorizonDict['ph01mcac_2'] = 139
        cHorizonDict['freeiron_l'] = 140
        cHorizonDict['freeiron_r'] = 141
        cHorizonDict['freeiron_h'] = 142
        cHorizonDict['feoxalate_'] = 143
        cHorizonDict['feoxalate1'] = 144
        cHorizonDict['feoxalat_1'] = 145
        cHorizonDict['extracid_l'] = 146
        cHorizonDict['extracid_r'] = 147
        cHorizonDict['extracid_h'] = 148
        cHorizonDict['extral_l'] = 149
        cHorizonDict['extral_r'] = 150
        cHorizonDict['extral_h'] = 151
        cHorizonDict['aloxalate_'] = 152
        cHorizonDict['aloxalate1'] = 153
        cHorizonDict['aloxalat_1'] = 154
        cHorizonDict['pbray1_l'] = 155
        cHorizonDict['pbray1_r'] = 156
        cHorizonDict['pbray1_h'] = 157
        cHorizonDict['poxalate_l'] = 158
        cHorizonDict['poxalate_r'] = 159
        cHorizonDict['poxalate_h'] = 160
        cHorizonDict['ph2osolubl'] = 161
        cHorizonDict['ph2osolu_1'] = 162
        cHorizonDict['ph2osolu_2'] = 163
        cHorizonDict['ptotal_l'] = 164
        cHorizonDict['ptotal_r'] = 165
        cHorizonDict['ptotal_h'] = 166
        cHorizonDict['excavdifcl'] = 167
        cHorizonDict['excavdifms'] = 168
        cHorizonDict['cokey'] = 169
        cHorizonDict['chkey'] = 170
        cHorizonDict['OBJECTID'] = 171
    
        return cHorizonDict

    def printNames(self):
        outKeyStr = ""
        for key in self.cHorizonDict:
            if outKeyStr == "":
                outKeyStr = key
            outKeyStr = outKeyStr + ", " + key

        print(outKeyStr)
