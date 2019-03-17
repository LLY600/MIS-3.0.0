''''
账单调整确认页面对象
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class BillAdjustConfirmPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.billAdjustConfirmItems = self.readConfigurationFile.getItemSection('billAdjustConfirm')
	def financialManagement(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.financialManagement'.lower()].split('>')
		financialManagement =getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def billAdjust(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.billAdjust'.lower()].split('>')
		billAdjust =getElement(self.driver, locateType, locateExpression)
		return billAdjust
	def billAdjustConfirm(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.billAdjustConfirm'.lower()].split('>')
		billAdjustConfirm =getElement(self.driver, locateType, locateExpression)
		return billAdjustConfirm
	def frameOfBillAdjustConfirm(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.frameOfBillAdjustConfirm'.lower()].split('>')
		frameOfBillAdjustConfirm =getElement(self.driver, locateType, locateExpression)
		return frameOfBillAdjustConfirm
	def contract(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.contract'.lower()].split('>')
		contract =getElement(self.driver, locateType, locateExpression)
		return contract
	def contractInput(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.contractInput'.lower()].split('>')
		contractInput =getElement(self.driver, locateType, locateExpression)
		return contractInput
	def contractSearch(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.contractSearch'.lower()].split('>')
		contractSearch =getElement(self.driver, locateType, locateExpression)
		return contractSearch
	def contractSearchResult(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.contractSearchResult'.lower()].split('>')
		contractSearchResult =getElement(self.driver, locateType, locateExpression)
		return contractSearchResult
	def search(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search
	def select(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.select'.lower()].split('>')
		select =getElement(self.driver, locateType, locateExpression)
		return select
	def confirmButton(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.confirmButton'.lower()].split('>')
		confirmButton =getElement(self.driver, locateType, locateExpression)
		return confirmButton
	def confirm(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def information(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
	def informationConfirm(self):
		locateType, locateExpression = self.billAdjustConfirmItems['billAdjustConfirm.informationConfirm'.lower()].split('>')
		informationConfirm =getElement(self.driver, locateType, locateExpression)
		return informationConfirm
