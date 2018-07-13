#!/usr/bin/python3
# @Time     : 2018-07-10
# @Author   : Ethan.Yin
# @File     : common.py
# @Software : PyCharm

import logging, os
import re
import visa
import time

#======================================
#Connect to instrument by MyVisa
#======================================
class MyVisa():
    def __init__(self, visaAddress, visaCommand, visaDLL=None, sleepTime = None, *args):
        self.address = visaAddress
        self.command = visaCommand
        self.visaDLL = 'c:/windows/system32/visa32.dll' if visaDLL is None else visaDLL
        self.sleepTime = 0.5 if sleepTime is None else sleepTime
        self.resourceManager = visa.ResourceManager(self.visaDLL)

    #Open a new resource
    def viOpen(self):
        self.instance = self.resourceManager.open_resource(self.address)
        time.sleep(self.sleepTime)

    #Close the specified resource
    def viClose(self):
        if self.instance is not None:
            self.instance.close()
            self.instance = None

    #To get the status of instrument
    def viQuery(self):
        self.instance.query(self.command)
        time.sleep(self.sleepTime)

    #To send command to instrument
    def viWrite(self):
        self.instance.write(self.command)
        time.sleep(self.sleepTime)

#======================================
#This is a common test utils
#======================================
class TestUtils:
    def __init__(self):
        print("==TestUtils==")

    #Return current system time
    def getCurrentTime(self):
        return time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))

    #Return current path
    def getCurrentPath(self):
        return os.path.dirname(__file__)

#========================================
#For user to log the logs by different levels
#Logger.debug - detailed information, typically fo interest only when diagnosing problems.
#Logger.info - confirmation that things are working as expected.
#Logger.war - an indication that something unexpected happened, or indicative of some problem in the near future. the software is still working as expected
#Logger.error - due to a more serious problem, the software has not been able to perform some function
#Logger.cri - a serious error, indicating that the program itself may be unable to continue running
#========================================
class Logger:
    def __init__(self, path, clevel = logging.DEBUG, flevel = logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        #Logs in console
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)

        #Logs in file
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(flevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def war(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)


