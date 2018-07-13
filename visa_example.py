# !/usr/bin/python3
# @Time     : 2018-07-10
# @Author   : Ethan.Yin
# @File     : visa_examply.py
# @Software : PyCharm


import visa
from common import Logger, TestUtils


if __name__ == '__main__':
    myInstr = INSTR_TCPIP('192.168.1.17')
    myInstr.open()
    myInstr.read_idn()
    myInstr.tran_file()
    myInstr.close()

"""Connect to instrument by TCPIP"""
class INSTR_TCPIP():
    def __init__(self, ip, visaDLL=None, *args):
        self.ip = ip
        self.visaDLL = 'c:/windows/system32/visa32.dll' if visaDLL is None else visaDLL
        self.address = 'TCPIP::%s::inst0::INSTR' % self.ip
        self.resourceManager = visa.ResourceManager(self.visaDLL)

    # Open a session to the specified resource 
    def open(self):
        self.instance = self.resourceManager.open_resource(self.address)
        self.instance.write('MMEM:STOR:SNP:FORM DB')

    # Close the specified session, event, or find list
    def close(self):
        if self.instance is not None:
            self.instance.close()
            self.instance = None


    def create_dir(self, path):
        print('MMEM:MDIR "%s"' % path)
        self.instance.write('MMEM:MDIR "%s"' % path)


    def recall_sta(self, filename):
        print('MMEM:LOAD "%s"' % filename)
        self.instance.write('MMEM:LOAD "%s"' % filename)
        # Time sleep in case of sta load uncompleted
        time.sleep(0.5)


    def wind_act(self, wind):
        self.instance.write('DISP:WIND%d:ACT' % wind)


    def wind_max(self, wind):
        self.instance.write('DISP:MAX %s' % wind)


    def trigger(self, status):
        cmdList = {'hold': 'OFF', 'continuous': 'ON'}
        self.instance.write('INIT1:CONT %s' % cmdList[status])


    def save_snp(self, name, n=2):
        print('MMEM:STOR:SNP "%s.s%dp"' % (name, n))
        self.instance.write('MMEM:STOR:SNP "%s.s%dp"' % (name, n))


    def save_image(self, imagname, fmt):
        assert fmt in ['jpg', 'png'], 'Invalid postfix of image'
        print('MMEM:STOR:IMAG "%s.%s"' % (imagname, fmt))
        self.instance.write('MMEM:STOR:IMAG "%s.%s"' % (imagname, fmt))


    def reset(self):
        self.instance.write('*RST')


    def read_idn(self):
        idn = self.instance.query('*IDN?')
        print(idn)
        return idn
    

    def read_data(self, wind=1, trac=1, axis='x'):
        posi = {'x': 'XAX?', 'y': 'FDAT?'}
        data = self.instance.query('CALC%d:TRAC%d:DATA:%s' % (wind, trac, posi[axis]))
        return eval(data)
    
    
    def tran_file(self):
        re = self.instance.query(":MMEM:TRAN? 'D:\\22.S2P'")
        with open("x.S2P", 'w') as f:
            f.write(re)
        print(type(re))




"""Connect to instrument by GPIB"""
class INSTR_GPIB():
    def __init__(self):
        self.address = 'GPIB0::8::INSTR'
        self.visaDll = 'c:/windows/system32/visa32.dll'
        self.resourceManager = visa.resourceManager(self.visaDll)

    def open(self):
        self.instance = resourceManager.open_resource(self.address)
        self.idn = self.instance.query('*IDN?')
        print(self.idn)


    def reset(self):
        self.instance.write('*RST')


    def set_dc(self):
        self.instance.write('CONF:CURR:DC AUTO, (@119, 120)')