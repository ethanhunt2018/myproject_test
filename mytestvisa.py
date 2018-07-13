#!/usr/bin/python3


# Check PyVisa is correctly installed yb starting up python, and creating a ResourceManager
import visa
from common import Logger, TestUtils


myLog = Logger('myLogs.log')
visaDll = 'c:/windows/system32/visa32.dll'
rm = visa.ResourceManager(visaDll)
myLog.info(rm.list_resources())

# Get current time
testUtils = TestUtils()
myLog.info(testUtils.getCurrentTime())

# Open the resource,
# '\*IDN?' it means "what are you", or "What's on your display at the moment?"
# my_instrument = rm.open_resource('GPIB0::14::INSTR')
# print(my_instrument.query('*IDN?'))



# Reading and writing values
# Data can be transferred in two ways: 1)ASCII, slow, human readable 2)Binary, fast, more difficult to debug.
