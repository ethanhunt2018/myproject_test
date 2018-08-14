#!/usr/bin/python3
# @Time     : 2018-07-10
# @Author   : Ethan.Yin
# @File     : common.py
# @Software : PyCharm

import logging, os
import re
import visa
import time
import xlrd
import xlsxwriter

#======================================
#Connect to instrument by MyVisa
#======================================
class MyVisa():
    def __init__(self, visaAddress, visaDLL=None, sleepTime = None, *args):
        self.address = visaAddress
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

    #Get the status of instrument
    def viQuery(self, command):
        self.instance.queryf(command)

    #Read the data from instrument
    def viRead(self, command):
        self.instance.read(command)

    #Send the command to instrument
    def viWrite(self, command):
        self.instance.write(command)
        time.sleep(self.sleepTime)


    """
    def read_memory(self, session, space, offset, width, extended=False):
    def write_memory(self, session, space, offset, data, width, extended=False):
    def move_in(self, session, space, offset, length, width, extended=False):
    def move_out(self, session, space, offset, length, data, width, extended=False):
    def peek(self, session, address, width):
    def poke(self, session, address, width, data):
    def assert_interrupt_signal(self, session, mode, status_id):
    def assert_trigger(self, session, protocol):
    def assert_utility_signal(self, session, line):
    def buffer_read(self, session, count):
    def buffer_write(self, session, data):
    def clear(self, session):
    def close(self, session):
    def disable_event(self, session, event_type, mechanism):
    def discard_events(self, session, event_type, mechanism):
    def enable_event(self, session, event_type, mechanism, context=None):
    def flush(self, session, mask):
    def get_attribute(self, session, attribute):
    def gpib_command(self, session, data):
    def gpib_control_atn(self, session, mode):
    def gpib_control_ren(self, session, mode):
    def gpib_pass_control(self, session, primary_address, secondary_address):
    def gpib_send_ifc(self, session):
    def in_8(self, session, space, offset, extended=False):
    def in_16(self, session, space, offset, extended=False):
    def in_32(self, session, space, offset, extended=False):
    def in_64(self, session, space, offset, extended=False):
    def install_handler(self, session, event_type, handler, user_handle):
    def list_resources(self, session, query='?*::INSTR'):
    def lock(self, session, lock_type, timeout, requested_key=None):
    def map_address(self, session, map_space, map_base, map_size,
    def map_trigger(self, session, trigger_source, trigger_destination, mode):
    def memory_allocation(self, session, size, extended=False):
    def memory_free(self, session, offset, extended=False):
    def move(self, session, source_space, source_offset, source_width, destination_space,
    def move_asynchronously(self, session, source_space, source_offset, source_width,
    def move_in_8(self, session, space, offset, length, extended=False):
    def move_in_16(self, session, space, offset, length, extended=False):
    def move_in_32(self, session, space, offset, length, extended=False):
    def move_in_64(self, session, space, offset, length, extended=False):
    def move_out_8(self, session, space, offset, length, data, extended=False):
    def move_out_16(self, session, space, offset, length, data, extended=False):
    def move_out_32(self, session, space, offset, length, data, extended=False):
    def move_out_64(self, session, space, offset, length, data, extended=False):
    def open(self, session, resource_name,
    def open_default_resource_manager(self):
    def out_8(self, session, space, offset, data, extended=False):
    def out_16(self, session, space, offset, data, extended=False):
    def out_32(self, session, space, offset, data, extended=False):
    def out_64(self, session, space, offset, data, extended=False):
    def parse_resource(self, session, resource_name):
    def parse_resource_extended(self, session, resource_name):
    def peek_8(self, session, address):
    def peek_16(self, session, address):
    def peek_32(self, session, address):
    def peek_64(self, session, address):
    def poke_8(self, session, address, data):
    def poke_16(self, session, address, data):
    def poke_32(self, session, address, data):
    def poke_64(self, session, address, data):
    def read(self, session, count):
    def read_asynchronously(self, session, count):
    def read_stb(self, session):
    def read_to_file(self, session, filename, count):
    def set_attribute(self, session, attribute, attribute_state):
    def set_buffer(self, session, mask, size):
    def status_description(self, session, status):
    def terminate(self, session, degree, job_id):
    def uninstall_handler(self, session, event_type, handler, user_handle=None):
    def unlock(self, session):
    def unmap_address(self, session):
    def unmap_trigger(self, session, trigger_source, trigger_destination):
    def usb_control_in(self, session, request_type_bitmap_field, request_id, request_value,
    def usb_control_out(self, session, request_type_bitmap_field, request_id, request_value,
    def vxi_command_query(self, session, mode, command):
    def wait_on_event(self, session, in_event_type, timeout):
    def write(self, session, data):
    def write_asynchronously(self, session, data):
    def write_from_file(self, session, filename, count):
    """

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


#========================================
#Parse and write Excel
#========================================
class ExcelHandler(object):
    def __init__(self, excelFile, sheetName):
        self.excelFile = excelFile
        self.sheetName = sheetName
        self.caseList = []

    #Input：the name of excel
    #Return：[], element is {}, every {} consists of ...
    def getCaseList(self):
        readExcel = xlrd.open_workbook(self.excelFile)
        try:
            table = readExcel.sheet_by_name(self.sheetName)
            for n in range(1,table.nrows):
                tmpdict = {}
                tmpdict['ID'] = table.cell(n,0).value
                tmpdict['Execution'] = table.cell(n,1).value
                tmpdict['CommandName'] = table.cell(n,2).value
                tmpdict['Command'] = table.cell(n,3).value
                tmpdict['ExpectedResult'] = table.cell(n,4).value
                self.caseList.append(tmpdict)
        except(RuntimeError, TypeError, NameError):
            raise
        finally:
            pass
        return self.caseList



    def writeCaseResult(self,resultBody,isSuccess,respTime,\
        excelFile,theRow,theCol=5):
        writeExcel = xlsxwriter.load_workbook(excelFile)
        try:
            wtable = writeExcel.get_sheet_by_name('Sheet1')
            wtable.cell(row=theRow+1,column=theCol+1).value = resultBody
            wtable.cell(row=theRow+1,column=theCol+2).value = isSuccess
            wtable.cell(row=theRow+1,column=theCol+3).value = respTime
            writeExcel.save(excelFile)
        except(RuntimeError, TypeError, NameError):
            raise
        finally:
            pass

