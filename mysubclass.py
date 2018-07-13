#!/usr/bin/python

class Parent:
    parentAttr = 100

    def __init__(self):
        print("Call parent constructed function")

    def parentMethod(self):
        print("Cal parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent property:", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("Call Child constructed function")

    def childMethod(self):
        print("Call Child method")

cTest = Child()
cTest.childMethod()
cTest.parentMethod()
cTest.setAttr(200)
cTest.getAttr()

