#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018-07-03
# @Author   : Ethan.Yin
# @File     : test.py
# @Software : PyCharm

import xlsxwriter, xlrd
import re
from common import TestUtils

testUtils = TestUtils()
myPath = testUtils.getCurrentPath()
print(myPath)

myInitFile = myPath + "\\test.xlsx"
print(myInitFile)

myWorkbook = xlrd.open_workbook(myInitFile)
mySheet = myWorkbook.sheet_by_name("PowerAnalyzer")

#print(mySheet._dimncols)
#print(mySheet._dimnrows)

#print(mySheet.nrows)
#print(mySheet.ncols)


myDict = {
    'clearESEandDSR':{},
    'registerESEToDecimalValue':{},
    'returnESEValue':{},
    'registerESRtoDecimalValue':{},
    'returnProductID':{},
    'resetUnitToDefaultSettings':{}
}
for row in range(0, mySheet.nrows):
    for column in range(0,mySheet.ncols):
        #print(mySheet.cell(row,column).value)
        for key in myDict.keys():
            if re.match(key, mySheet.cell(row,0).value) and re.match('Command',mySheet.cell(0,column).value):
                myDict[key]['Command'] =  mySheet.cell(row,column).value
            if re.match(key, mySheet.cell(row,0).value) and re.match('Expectation',mySheet.cell(0,column).value):
                myDict[key]['Expectation'] = mySheet.cell(row,column).value


print(myDict)
