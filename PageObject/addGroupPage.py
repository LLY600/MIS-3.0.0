'''
添加集团页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddGroupPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addGroupItems = self.readConfigurationFile.getItemSection('addGroup')
	def tenancyManagement(self):
		locateType, locateExpression = self.addGroupItems['addGroup.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def propertyManagement(self):
		locateType, locateExpression = self.addGroupItems['addGroup.propertyManagement'.lower()].split('>')
		propertyManagement =getElement(self.driver, locateType, locateExpression)
		return propertyManagement
	def groupManagement(self):
		locateType, locateExpression = self.addGroupItems['addGroup.groupManagement'.lower()].split('>')
		groupManagement =getElement(self.driver, locateType, locateExpression)
		return groupManagement
	def frameOfGroupManagement(self):
		locateType, locateExpression = self.addGroupItems['addGroup.frameOfGroupManagement'.lower()].split('>')
		frameOfGroupManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfGroupManagement
	def add(self):
		locateType, locateExpression = self.addGroupItems['addGroup.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddGroupManagement(self):
		locateType, locateExpression = self.addGroupItems['addGroup.frameOfAddGroupManagement'.lower()].split('>')
		frameOfAddGroupManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfAddGroupManagement
	def groupNum(self):
		locateType, locateExpression = self.addGroupItems['addGroup.groupNum'.lower()].split('>')
		groupNum =getElement(self.driver, locateType, locateExpression)
		return groupNum
	def groupName(self):
		locateType, locateExpression = self.addGroupItems['addGroup.groupName'.lower()].split('>')
		groupName =getElement(self.driver, locateType, locateExpression)
		return groupName
	def save(self):
		locateType, locateExpression = self.addGroupItems['addGroup.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addGroupItems['addGroup.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text