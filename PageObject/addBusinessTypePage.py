'''
添加业态页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddBusinessTypePage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addBusinessTypeItems = self.readConfigurationFile.getItemSection('addBusinessType')
	def tenancyManagement(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def basicSetting(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.basicSetting'.lower()].split('>')
		basicSetting =getElement(self.driver, locateType, locateExpression)
		return basicSetting
	def businessTypeManagement(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.businessTypeManagement'.lower()].split('>')
		businessTypeManagement =getElement(self.driver, locateType, locateExpression)
		return businessTypeManagement
	def frameOfBusinessTypeManagement(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.frameOfBusinessTypeManagement'.lower()].split('>')
		frameOfBusinessTypeManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfBusinessTypeManagement
	def add(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddBusinessType(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.frameOfAddBusinessType'.lower()].split('>')
		frameOfAddBusinessType =getElement(self.driver, locateType, locateExpression)
		return frameOfAddBusinessType
	def businessTypeNumBox(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.businessTypeNumBox'.lower()].split('>')
		businessTypeNumBox =getElement(self.driver, locateType, locateExpression)
		return businessTypeNumBox
	def businessTypeNum(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.businessTypeNum'.lower()].split('>')
		businessTypeNum =getElement(self.driver, locateType, locateExpression)
		return businessTypeNum
	def businessTypeNameBox(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.businessTypeNameBox'.lower()].split('>')
		businessTypeNameBox =getElement(self.driver, locateType, locateExpression)
		return businessTypeNameBox
	def businessTypeName(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.businessTypeName'.lower()].split('>')
		businessTypeName =getElement(self.driver, locateType, locateExpression)
		return businessTypeName
	def save(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addBusinessTypeItems['addBusinessType.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text