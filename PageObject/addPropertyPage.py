'''
添加物业性质页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddPropertyPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addPropertyItems = self.readConfigurationFile.getItemSection('addProperty')
	def tenancyManagement(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def basicSetting(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.basicSetting'.lower()].split('>')
		basicSetting =getElement(self.driver, locateType, locateExpression)
		return basicSetting
	def propertyManagement(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.propertyManagement'.lower()].split('>')
		propertyManagement =getElement(self.driver, locateType, locateExpression)
		return propertyManagement
	def frameOfPropertyManagement(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.frameOfPropertyManagement'.lower()].split('>')
		frameOfPropertyManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfPropertyManagement
	def add(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddProperty(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.frameOfAddProperty'.lower()].split('>')
		frameOfAddProperty =getElement(self.driver, locateType, locateExpression)
		return frameOfAddProperty
	def propertyNumBox(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.propertyNumBox'.lower()].split('>')
		propertyNumBox =getElement(self.driver, locateType, locateExpression)
		return propertyNumBox
	def propertyNum(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.propertyNum'.lower()].split('>')
		propertyNum =getElement(self.driver, locateType, locateExpression)
		return propertyNum
	def propertyNameBox(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.propertyNameBox'.lower()].split('>')
		propertyNameBox =getElement(self.driver, locateType, locateExpression)
		return propertyNameBox
	def propertyName(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.propertyName'.lower()].split('>')
		propertyName =getElement(self.driver, locateType, locateExpression)
		return propertyName
	def save(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addPropertyItems['addProperty.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text