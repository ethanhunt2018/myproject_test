#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018-07-19
# @Author   : Ethan.Yin
# @File     : main.py
# @Software : PyCharm

import os
from _common.common import *
from _reports.testcase import *
from _reports.testreport import *

if __name__ == '__main__':

    #Initialize VISA information
    visaAddress = 'GPIB0::8::INSTR'
    visaDll = 'c:/windows/system32/visa32.dll'
    rm = MyVisa(visaAddress, visaDll)

    #Get current path
    myPath = os.path.dirname(__file__)

    #Enable test utils
    testUtils = TestUtils()

    #Get current time
    currentTime = testUtils.getCurrentTime()

    #Set logs file
    logsFile = myPath + '\\_logs\\logs' + currentTime.replace(':','') + '.log'
    myLogger = Logger(logsFile)

    #Set test report file
    myTestReports = myPath + '\\_reports\\reports\\TestReport' + currentTime.replace(':','') + '.html'

    #=======================================
    # Start testing
    #=======================================
    myLogger.info("=======Start Testing======")
    myLogger.info("Initialization....")
    myLogger.info(logsFile)
    myLogger.info(myTestReports)

    #Read Test Cases
    myLogger.info("Import test cases")
    caselist = []
    myInitFile = myPath + '\\_cases\\test.xlsx'
    myExcel = ExcelHandler(myInitFile, "PowerAnalyzer")
    caselist = myExcel.getCaseList()
    myLogger.debug(caselist)



    #Execution cases
    #=============================================
    myLogger.info("Execute test cases one by one")
    time.sleep(5)
    #=============================================


    #Start to write test reports by Python unittest module
    myLogger.info("start to write test report")
    #print(myTestReports)
    fp = open(myTestReports,'wb')

    #generate the title of report
    runner = HTMLTestRunner(
        stream=fp,
        title='Test Report',
        #description='detailed test results',
        tester='EthanYin'
        )

    #write the test results into report
    runner.run(Suite())

    #close the file
    fp.close()
    myLogger.info("Test reports generation is done")
    myLogger.info("======End======")
    #=======================================
    # End
    #=======================================




















