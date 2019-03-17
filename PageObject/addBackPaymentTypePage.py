'''
添加后台收款方式页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddBackPaymentTypePage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)
		self.readConfigurationFile = readConfigurationFile()
		self.addBackPaymentTypeItems = self.readConfigurationFile.getItemSection('addBackPaymentType')
	def financialManagement(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.financialManagement'.lower()].split('>')
		financialManagement =getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def basicSetting(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.basicSetting'.lower()].split('>')
		basicSetting =getElement(self.driver, locateType, locateExpression)
		return basicSetting
	def backPaymentType(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.backPaymentType'.lower()].split('>')
		backPaymentType =getElement(self.driver, locateType, locateExpression)
		return backPaymentType
	def frameOfBackPaymentType(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.frameOfBackPaymentType'.lower()].split('>')
		frameOfBackPaymentType =getElement(self.driver, locateType, locateExpression)
		return frameOfBackPaymentType
	def add(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddBackPaymentType(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.frameOfAddBackPaymentType'.lower()].split('>')
		frameOfAddBackPaymentType =getElement(self.driver, locateType, locateExpression)
		return frameOfAddBackPaymentType
	def paymentTypeNumBox(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.paymentTypeNumBox'.lower()].split('>')
		paymentTypeNumBox =getElement(self.driver, locateType, locateExpression)
		return paymentTypeNumBox
	def paymentTypeNum(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.paymentTypeNum'.lower()].split('>')
		paymentTypeNum =getElement(self.driver, locateType, locateExpression)
		return paymentTypeNum
	def paymentTypeBox(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.paymentTypeBox'.lower()].split('>')
		paymentTypeBox =getElement(self.driver, locateType, locateExpression)
		return paymentTypeBox
	def paymentType(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.paymentType'.lower()].split('>')
		paymentType =getElement(self.driver, locateType, locateExpression)
		return paymentType
	def save(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addBackPaymentTypeItems['addBackPaymentType.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text