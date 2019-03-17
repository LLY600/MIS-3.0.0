'''
账单生成页面对象
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class BillGenerationPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.billGenerationItems = self.readConfigurationFile.getItemSection('billGeneration')
	def financialManagement(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.financialManagement'.lower()].split('>')
		financialManagement =getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def billManagement(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.billManagement'.lower()].split('>')
		billManagement =getElement(self.driver, locateType, locateExpression)
		return billManagement
	def billGeneration(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.billGeneration'.lower()].split('>')
		billGeneration =getElement(self.driver, locateType, locateExpression)
		return billGeneration
	def frameOfBillGeneration(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.frameOfBillGeneration'.lower()].split('>')
		frameOfBillGeneration =getElement(self.driver, locateType, locateExpression)
		return frameOfBillGeneration
	def settlementDate(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.settlementDate'.lower()].split('>')
		settlementDate =getElement(self.driver, locateType, locateExpression)
		return settlementDate
	def contractName(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.contractName'.lower()].split('>')
		contractName =getElement(self.driver, locateType, locateExpression)
		return contractName
	def contractNameInput(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.contractNameInput'.lower()].split('>')
		contractNameInput =getElement(self.driver, locateType, locateExpression)
		return contractNameInput
	def contractNameSearch(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.contractNameSearch'.lower()].split('>')
		contractNameSearch =getElement(self.driver, locateType, locateExpression)
		return contractNameSearch
	def contractNameSearchResult(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.contractNameSearchResult'.lower()].split('>')
		contractNameSearchResult =getElement(self.driver, locateType, locateExpression)
		return contractNameSearchResult
	def button(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.button'.lower()].split('>')
		button =getElement(self.driver, locateType, locateExpression)
		return button
	def confirm(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def information(self):
		locateType, locateExpression = self.billGenerationItems['billGeneration.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
