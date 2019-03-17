'''
添加账单调整类型页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddBillAdjustTypePage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)
		self.readConfigurationFile = readConfigurationFile()
		self.addBillAdjustTypeItems = self.readConfigurationFile.getItemSection('addBillAdjustType')
	def financialManagement(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.financialManagement'.lower()].split('>')
		financialManagement =getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def billAdjust(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.billAdjust'.lower()].split('>')
		billAdjust =getElement(self.driver, locateType, locateExpression)
		return billAdjust
	def billAdjustType(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.billAdjustType'.lower()].split('>')
		billAdjustType =getElement(self.driver, locateType, locateExpression)
		return billAdjustType
	def frameOfBillAdjustType(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.frameOfBillAdjustType'.lower()].split('>')
		frameOfBillAdjustType =getElement(self.driver, locateType, locateExpression)
		return frameOfBillAdjustType
	def add(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddBillAdjust(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.frameOfAddBillAdjust'.lower()].split('>')
		frameOfAddBillAdjust =getElement(self.driver, locateType, locateExpression)
		return frameOfAddBillAdjust
	def billAdjustNumBox(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.billAdjustNumBox'.lower()].split('>')
		billAdjustNumBox =getElement(self.driver, locateType, locateExpression)
		return billAdjustNumBox
	def billAdjustNum(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.billAdjustNum'.lower()].split('>')
		billAdjustNum =getElement(self.driver, locateType, locateExpression)
		return billAdjustNum
	def billAdjustNameBox(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.billAdjustNameBox'.lower()].split('>')
		billAdjustNameBox =getElement(self.driver, locateType, locateExpression)
		return billAdjustNameBox
	def billAdjustName(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.billAdjustName'.lower()].split('>')
		billAdjustName =getElement(self.driver, locateType, locateExpression)
		return billAdjustName
	def save(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addBillAdjustTypeItems['addBillAdjustType.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text