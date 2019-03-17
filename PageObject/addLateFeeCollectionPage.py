'''
滞纳金收款页面对象
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddLateFeeCollectionPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addLateFeeCollectionItems = self.readConfigurationFile.getItemSection('addLateFeeCollection')
	def financialManagement(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.financialManagement'.lower()].split('>')
		financialManagement =getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def lateFeeManagement(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.lateFeeManagement'.lower()].split('>')
		lateFeeManagement =getElement(self.driver, locateType, locateExpression)
		return lateFeeManagement
	def lateFeeCollection(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.lateFeeCollection'.lower()].split('>')
		lateFeeCollection =getElement(self.driver, locateType, locateExpression)
		return lateFeeCollection
	def frameOfLateFeeCollection(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.frameOfLateFeeCollection'.lower()].split('>')
		frameOfLateFeeCollection =getElement(self.driver, locateType, locateExpression)
		return frameOfLateFeeCollection
	def add(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddLateFeeCollection(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.frameOfAddLateFeeCollection'.lower()].split('>')
		frameOfAddLateFeeCollection =getElement(self.driver, locateType, locateExpression)
		return frameOfAddLateFeeCollection
	def merchant(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.merchant'.lower()].split('>')
		merchant =getElement(self.driver, locateType, locateExpression)
		return merchant
	def merchantInput(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.merchantInput'.lower()].split('>')
		merchantInput =getElement(self.driver, locateType, locateExpression)
		return merchantInput
	def merchantSearch(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.merchantSearch'.lower()].split('>')
		merchantSearch =getElement(self.driver, locateType, locateExpression)
		return merchantSearch
	def merchantSearchResult(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.merchantSearchResult'.lower()].split('>')
		merchantSearchResult =getElement(self.driver, locateType, locateExpression)
		return merchantSearchResult
	def contract(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.contract'.lower()].split('>')
		contract =getElement(self.driver, locateType, locateExpression)
		return contract
	def contractInput(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.contractInput'.lower()].split('>')
		contractInput =getElement(self.driver, locateType, locateExpression)
		return contractInput
	def contractSearch(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.contractSearch'.lower()].split('>')
		contractSearch =getElement(self.driver, locateType, locateExpression)
		return contractSearch
	def contractSearchResult(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.contractSearchResult'.lower()].split('>')
		contractSearchResult =getElement(self.driver, locateType, locateExpression)
		return contractSearchResult
	def lateFeeNum(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.lateFeeNum'.lower()].split('>')
		lateFeeNum =getElement(self.driver, locateType, locateExpression)
		return lateFeeNum
	def lateFeeNumInput(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.lateFeeNumInput'.lower()].split('>')
		lateFeeNumInput =getElement(self.driver, locateType, locateExpression)
		return lateFeeNumInput
	def lateFeeSearch(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.lateFeeSearch'.lower()].split('>')
		lateFeeSearch =getElement(self.driver, locateType, locateExpression)
		return lateFeeSearch
	def lateFeeSearchResult(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.lateFeeSearchResult'.lower()].split('>')
		lateFeeSearchResult =getElement(self.driver, locateType, locateExpression)
		return lateFeeSearchResult
	def paymentTime(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.paymentTime'.lower()].split('>')
		paymentTime =getElement(self.driver, locateType, locateExpression)
		return paymentTime
	def feeType(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.feeType'.lower()].split('>')
		feeType =getElement(self.driver, locateType, locateExpression)
		return feeType
	def feeTypeSelect1(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.feeTypeSelect1'.lower()].split('>')
		feeTypeSelect1 =getElement(self.driver, locateType, locateExpression)
		return feeTypeSelect1
	def feeTypeSelect2(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.feeTypeSelect2'.lower()].split('>')
		feeTypeSelect2 =getElement(self.driver, locateType, locateExpression)
		return feeTypeSelect2
	def feeTypeSelect3(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.feeTypeSelect3'.lower()].split('>')
		feeTypeSelect3 =getElement(self.driver, locateType, locateExpression)
		return feeTypeSelect3
	def addRow(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.addRow'.lower()].split('>')
		addRow =getElement(self.driver, locateType, locateExpression)
		return addRow
	def collectionTypeBox(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.collectionTypeBox'.lower()].split('>')
		collectionTypeBox =getElement(self.driver, locateType, locateExpression)
		return collectionTypeBox
	def collectionTypeBoxInner(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.collectionTypeBoxInner'.lower()].split('>')
		collectionTypeBoxInner =getElement(self.driver, locateType, locateExpression)
		return collectionTypeBoxInner
	def collectionType(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.collectionType'.lower()].split('>')
		collectionType =getElement(self.driver, locateType, locateExpression)
		return collectionType
	def collectionMoneyBox(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.collectionMoneyBox'.lower()].split('>')
		collectionMoneyBox =getElement(self.driver, locateType, locateExpression)
		return collectionMoneyBox
	def collectionMoney(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.collectionMoney'.lower()].split('>')
		collectionMoney =getElement(self.driver, locateType, locateExpression)
		return collectionMoney
	def deductMoneyBox(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.deductMoneyBox'.lower()].split('>')
		deductMoneyBox =getElement(self.driver, locateType, locateExpression)
		return deductMoneyBox
	def deductMoney(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.deductMoney'.lower()].split('>')
		deductMoney =getElement(self.driver, locateType, locateExpression)
		return deductMoney
	def save(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def confirm(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def information(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
	def informationConfirm(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.informationConfirm'.lower()].split('>')
		informationConfirm =getElement(self.driver, locateType, locateExpression)
		return informationConfirm
	def contractOfList(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.contractOfList'.lower()].split('>')
		contractOfList =getElement(self.driver, locateType, locateExpression)
		return contractOfList
	def contractInputOfList(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.contractInputOfList'.lower()].split('>')
		contractInputOfList =getElement(self.driver, locateType, locateExpression)
		return contractInputOfList
	def contractSearchOfList(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.contractSearchOfList'.lower()].split('>')
		contractSearchOfList =getElement(self.driver, locateType, locateExpression)
		return contractSearchOfList
	def contractSearchResultOfList(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.contractSearchResultOfList'.lower()].split('>')
		contractSearchResultOfList =getElement(self.driver, locateType, locateExpression)
		return contractSearchResultOfList
	def search(self):
		locateType, locateExpression = self.addLateFeeCollectionItems['addLateFeeCollection.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search