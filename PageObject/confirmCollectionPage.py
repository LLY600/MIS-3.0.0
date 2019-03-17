'''
收款确认页面对象
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddCollectionConfirmPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.collectionConfirmItems = self.readConfigurationFile.getItemSection('addCollectionConfirm')
	def financialManagement(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.financialManagement'.lower()].split('>')
		financialManagement =getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def collectionManagement(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.collectionManagement'.lower()].split('>')
		collectionManagement =getElement(self.driver, locateType, locateExpression)
		return collectionManagement
	def collectionConfirm(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.collectionConfirm'.lower()].split('>')
		collectionConfirm =getElement(self.driver, locateType, locateExpression)
		return collectionConfirm
	def frameOfCollectionConfirm(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.frameOfCollectionConfirm'.lower()].split('>')
		frameOfCollectionConfirm =getElement(self.driver, locateType, locateExpression)
		return frameOfCollectionConfirm
	def contract(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.contract'.lower()].split('>')
		contract =getElement(self.driver, locateType, locateExpression)
		return contract
	def contractInput(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.contractInput'.lower()].split('>')
		contractInput =getElement(self.driver, locateType, locateExpression)
		return contractInput
	def contractSearch(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.contractSearch'.lower()].split('>')
		contractSearch =getElement(self.driver, locateType, locateExpression)
		return contractSearch
	def contractSearchResult(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.contractSearchResult'.lower()].split('>')
		contractSearchResult =getElement(self.driver, locateType, locateExpression)
		return contractSearchResult
	def collectionType(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.collectionType'.lower()].split('>')
		collectionType =getElement(self.driver, locateType, locateExpression)
		return collectionType
	def collectionTypeSelect(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.collectionTypeSelect'.lower()].split('>')
		collectionTypeSelect =getElement(self.driver, locateType, locateExpression)
		return collectionTypeSelect
	def search(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search
	def select(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.select'.lower()].split('>')
		select =getElement(self.driver, locateType, locateExpression)
		return select
	def confirm(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def confirmCollection(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.confirmCollection'.lower()].split('>')
		confirmCollection =getElement(self.driver, locateType, locateExpression)
		return confirmCollection
	def information(self):
		locateType, locateExpression = self.collectionConfirmItems['addCollectionConfirm.infomation'.lower()].split('>')
		infomation =getElement(self.driver, locateType, locateExpression)
		return infomation.text