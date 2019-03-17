'''
添加结算组别页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddSettlementGroupPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addSettlementGroupItems = self.readConfigurationFile.getItemSection('addSettlementGroup')
	def tenancyManagement(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.financialManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def basicSetting(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.basicSetting'.lower()].split('>')
		basicSetting =getElement(self.driver, locateType, locateExpression)
		return basicSetting
	def settlementGroupManagement(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.settlementGroupManagement'.lower()].split('>')
		settlementGroupManagement =getElement(self.driver, locateType, locateExpression)
		return settlementGroupManagement
	def frameOfSettlementGroupManagement(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.frameOfSettlementGroupManagement'.lower()].split('>')
		frameOfSettlementGroupManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfSettlementGroupManagement
	def add(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddSettlementGroup(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.frameOfAddSettlementGroup'.lower()].split('>')
		frameOfAddSettlementGroup =getElement(self.driver, locateType, locateExpression)
		return frameOfAddSettlementGroup
	def settlementGroupNumBox(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.settlementGroupNumBox'.lower()].split('>')
		settlementGroupNumBox =getElement(self.driver, locateType, locateExpression)
		return settlementGroupNumBox
	def settlementGroupNum(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.settlementGroupNum'.lower()].split('>')
		settlementGroupNum =getElement(self.driver, locateType, locateExpression)
		return settlementGroupNum
	def settlementGroupNameBox(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.settlementGroupNameBox'.lower()].split('>')
		settlementGroupNameBox =getElement(self.driver, locateType, locateExpression)
		return settlementGroupNameBox
	def settlementGroupName(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.settlementGroupName'.lower()].split('>')
		settlementGroupName =getElement(self.driver, locateType, locateExpression)
		return settlementGroupName
	def save(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
	def confirm(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def search(self):
		locateType, locateExpression = self.addSettlementGroupItems['addSettlementGroup.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search