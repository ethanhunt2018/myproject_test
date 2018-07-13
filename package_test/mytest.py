
import time, re

def curr_time():
    currenttime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    return currenttime


#dict = {}
#dict = {'clearESEandDSR':{'command':'*CLS', 'expectation':True},'registerESEToDecimalValue':{'command':'*ESE','expectation': True}}


#print(dict['clearESEandDSR']['command'])
#print(dict['clearESEandDSR']['expectation'])

#print(dict['registerESEToDecimalValue']['command'])
#print(dict['registerESEToDecimalValue']['expectation'])


myDict = {
    'clearESEandDSR':{},
    'registerESEToDecimalValue':{},
    'returnESEValue':{},
    'registerESRtoDecimalValue':{},
    'returnProductID':{},
    'resetUnitToDefaultSettings':{}
}

#print(myDict.keys())

for keys in myDict.keys():
    #print(keys)
    if re.match(keys, 'clearESEandDSR'):
        print("CORRECT")
        myDict[keys] = {'command':"*ISD", 'expectation':True}
        print(myDict[keys])
    else:
        print("ERROR")

print(myDict['clearESEandDSR']['command'])
print(myDict['clearESEandDSR']['expectation'])
