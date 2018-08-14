#!/usr/bin/python3

import unittest

class Project1(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def t_001(self):
        self.assertEqual("TRUE","TRUE","clearESEandDSR, expected Reuslt is wrong")

    def t_002(self):
        self.assertEqual("<NR1>","","registerESEToDecimalValue, expected Reuslt is wrong")

    def t_003(self):
        self.assertEqual("TRUE","TRUE","returnESEValue, expected Reuslt is wrong")

    def t_004(self):
        self.assertEqual("TRUE","TRUE","registerESRtoDecimalValue, expected Reuslt is wrong")

    def t_005(self):
        self.assertEqual("TRUE","TRUE","returnProductID, expected Reuslt is wrong")

    def t_006(self):
        self.assertEqual("TRUE","TRUE","resetUnitToDefaultSettings, expected Reuslt is wrong")

    def t_007(self):
        self.assertEqual("TRUE","TRUE","enableOperationComplete, expected Reuslt is wrong")

    def t_008(self):
        self.assertEqual(1,0,"operationCompleteState, expected Reuslt is wrong")

    def t_009(self):
        self.assertEqual("<CRD>","","returnOperationNumber, expected Reuslt is wrong")

    def t_010(self):
        pass

class Project2(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def t_011(self):
        self.assertEqual("TRUE","TRUE","powerOnStatus, expected Reuslt is wrong")

    def t_012(self):
        self.assertEqual("TRUE","TRUE","recallInstrumentstate, expected Reuslt is wrong")

    def t_013(self):
        self.assertEqual("<NR1>","","setServiceRequest, expected Reuslt is wrong")

    def t_014(self):
        self.assertEqual("TRUE","TRUE","reset, expected Reuslt is wrong")

    def t_015(self):
        self.assertEqual("TRUE","TRUE","saveInstrumentSate, expected Reuslt is wrong")

    def t_016(self):
        self.assertEqual("TRUE","TRUE","enableServiceRequest, expected Reuslt is wrong")

    def t_017(self):
        self.assertEqual("TRUE","TRUE","returnServiceRequest, expected Reuslt is wrong")

    def t_018(self):
        self.assertEqual(1,0,"returnStatusByte, expected Reuslt is wrong")

    def t_019(self):
        self.assertEqual("TRUE","TRUE","trigger, expected Reuslt is wrong")

    def t_020(self):
        pass

#Add all test cases into suit()
def Suite():
    #define a suit
    suiteTest = unittest.TestSuite()
    #add cases into suit
    suiteTest.addTest(Project1("t_001"))
    suiteTest.addTest(Project1("t_002"))
    suiteTest.addTest(Project1("t_003"))
    suiteTest.addTest(Project1("t_004"))
    suiteTest.addTest(Project1("t_005"))
    suiteTest.addTest(Project1("t_006"))
    suiteTest.addTest(Project1("t_007"))
    suiteTest.addTest(Project1("t_008"))
    suiteTest.addTest(Project1("t_009"))
    suiteTest.addTest(Project1("t_010"))
    suiteTest.addTest(Project2("t_011"))
    suiteTest.addTest(Project2("t_012"))
    suiteTest.addTest(Project2("t_013"))
    suiteTest.addTest(Project2("t_014"))
    suiteTest.addTest(Project2("t_015"))
    suiteTest.addTest(Project2("t_016"))
    suiteTest.addTest(Project2("t_017"))
    suiteTest.addTest(Project2("t_018"))
    suiteTest.addTest(Project2("t_019"))
    suiteTest.addTest(Project2("t_020"))
    return suiteTest
