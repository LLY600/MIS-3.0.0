'''
滞纳金收款确认页面对象
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddLateFeeCollectionConfirmPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.lateFeeCollectionConfirmItems = self.readConfigurationFile.getItemSection('addLateFeeCollectionConfirm')
	def financialManagement(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.financialManagement'.lower()].split('>')
		financialManagement =getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def lateFeeManagement(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.lateFeeManagement'.lower()].split('>')
		lateFeeManagement =getElement(self.driver, locateType, locateExpression)
		return lateFeeManagement
	def lateFeeCollectionConfirm(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.lateFeeCollectionConfirm'.lower()].split('>')
		lateFeeCollectionConfirm =getElement(self.driver, locateType, locateExpression)
		return lateFeeCollectionConfirm
	def frameOfLateFeeCollectionConfirm(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.frameOfLateFeeCollectionConfirm'.lower()].split('>')
		frameOfLateFeeCollectionConfirm =getElement(self.driver, locateType, locateExpression)
		return frameOfLateFeeCollectionConfirm
	def contract(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.contract'.lower()].split('>')
		contract =getElement(self.driver, locateType, locateExpression)
		return contract
	def contractInput(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.contractInput'.lower()].split('>')
		contractInput =getElement(self.driver, locateType, locateExpression)
		return contractInput
	def contractSearch(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.contractSearch'.lower()].split('>')
		contractSearch =getElement(self.driver, locateType, locateExpression)
		return contractSearch
	def contractSearchResult(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.contractSearchResult'.lower()].split('>')
		contractSearchResult =getElement(self.driver, locateType, locateExpression)
		return contractSearchResult
	def search(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search
	def select(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.select'.lower()].split('>')
		select =getElement(self.driver, locateType, locateExpression)
		return select
	def confirm(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def confirmCollection(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.confirmCollection'.lower()].split('>')
		confirmCollection =getElement(self.driver, locateType, locateExpression)
		return confirmCollection
	def information(self):
		locateType, locateExpression = self.lateFeeCollectionConfirmItems['addLateFeeCollectionConfirm.infomation'.lower()].split('>')
		infomation =getElement(self.driver, locateType, locateExpression)
		return infomation.text