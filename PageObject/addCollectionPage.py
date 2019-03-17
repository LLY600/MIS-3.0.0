'''
收款维护页面对象
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddCollectionPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addCollectionItems = self.readConfigurationFile.getItemSection('addCollection')
	def financialManagement(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.financialManagement'.lower()].split('>')
		financialManagement =getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def collectionManagement(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.collectionManagement'.lower()].split('>')
		collectionManagement =getElement(self.driver, locateType, locateExpression)
		return collectionManagement
	def collectionMaintain(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.collectionMaintain'.lower()].split('>')
		collectionMaintain =getElement(self.driver, locateType, locateExpression)
		return collectionMaintain
	def frameOfCollectionMaintain(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.frameOfCollectionMaintain'.lower()].split('>')
		frameOfCollectionMaintain =getElement(self.driver, locateType, locateExpression)
		return frameOfCollectionMaintain
	def add(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddCollection(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.frameOfAddCollection'.lower()].split('>')
		frameOfAddCollection =getElement(self.driver, locateType, locateExpression)
		return frameOfAddCollection
	def merchant(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.merchant'.lower()].split('>')
		merchant =getElement(self.driver, locateType, locateExpression)
		return merchant
	def merchantInput(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.merchantInput'.lower()].split('>')
		merchantInput =getElement(self.driver, locateType, locateExpression)
		return merchantInput
	def merchantSearch(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.merchantSearch'.lower()].split('>')
		merchantSearch =getElement(self.driver, locateType, locateExpression)
		return merchantSearch
	def merchantSearchResult(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.merchantSearchResult'.lower()].split('>')
		merchantSearchResult =getElement(self.driver, locateType, locateExpression)
		return merchantSearchResult
	def contract(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.contract'.lower()].split('>')
		contract =getElement(self.driver, locateType, locateExpression)
		return contract
	def contractInput(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.contractInput'.lower()].split('>')
		contractInput =getElement(self.driver, locateType, locateExpression)
		return contractInput
	def contractSearch(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.contractSearch'.lower()].split('>')
		contractSearch =getElement(self.driver, locateType, locateExpression)
		return contractSearch
	def contractSearchResult(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.contractSearchResult'.lower()].split('>')
		contractSearchResult =getElement(self.driver, locateType, locateExpression)
		return contractSearchResult
	def paymentTime(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.paymentTime'.lower()].split('>')
		paymentTime =getElement(self.driver, locateType, locateExpression)
		return paymentTime
	def settlementGroup(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.settlementGroup'.lower()].split('>')
		settlementGroup =getElement(self.driver, locateType, locateExpression)
		return settlementGroup
	def settlementGroupInput(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.settlementGroupInput'.lower()].split('>')
		settlementGroupInput =getElement(self.driver, locateType, locateExpression)
		return settlementGroupInput
	def settlementGroupSearch(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.settlementGroupSearch'.lower()].split('>')
		settlementGroupSearch =getElement(self.driver, locateType, locateExpression)
		return settlementGroupSearch
	def settlementGroupResult(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.settlementGroupResult'.lower()].split('>')
		settlementGroupResult =getElement(self.driver, locateType, locateExpression)
		return settlementGroupResult
	def billNum(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.billNum'.lower()].split('>')
		billNum =getElement(self.driver, locateType, locateExpression)
		return billNum
	def billNumInput(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.billNumInput'.lower()].split('>')
		billNumInput =getElement(self.driver, locateType, locateExpression)
		return billNumInput
	def billNumSearch(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.billNumSearch'.lower()].split('>')
		billNumSearch =getElement(self.driver, locateType, locateExpression)
		return billNumSearch
	def billNumSearchResult(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.billNumSearchResult'.lower()].split('>')
		billNumSearchResult =getElement(self.driver, locateType, locateExpression)
		return billNumSearchResult
	def costItem(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.costItem'.lower()].split('>')
		costItem =getElement(self.driver, locateType, locateExpression)
		return costItem
	def addRow(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.addRow'.lower()].split('>')
		addRow =getElement(self.driver, locateType, locateExpression)
		return addRow
	def collectionTypeBox(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.collectionTypeBox'.lower()].split('>')
		collectionTypeBox =getElement(self.driver, locateType, locateExpression)
		return collectionTypeBox
	def collectionTypeBoxInner(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.collectionTypeBoxInner'.lower()].split('>')
		collectionTypeBoxInner =getElement(self.driver, locateType, locateExpression)
		return collectionTypeBoxInner
	def collectionType(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.collectionType'.lower()].split('>')
		collectionType =getElement(self.driver, locateType, locateExpression)
		return collectionType
	def collectionMoneyBox(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.collectionMoneyBox'.lower()].split('>')
		collectionMoneyBox =getElement(self.driver, locateType, locateExpression)
		return collectionMoneyBox
	def collectionMoney(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.collectionMoney'.lower()].split('>')
		collectionMoney =getElement(self.driver, locateType, locateExpression)
		return collectionMoney
	def deductMoneyBox(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.deductMoneyBox'.lower()].split('>')
		deductMoneyBox =getElement(self.driver, locateType, locateExpression)
		return deductMoneyBox
	def deductMoney(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.deductMoney'.lower()].split('>')
		deductMoney =getElement(self.driver, locateType, locateExpression)
		return deductMoney
	def save(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def confirm(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def information(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
	def informationConfirm(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.informationConfirm'.lower()].split('>')
		informationConfirm =getElement(self.driver, locateType, locateExpression)
		return informationConfirm
	def contractOfList(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.contractOfList'.lower()].split('>')
		contractOfList =getElement(self.driver, locateType, locateExpression)
		return contractOfList
	def contractInputOfList(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.contractInputOfList'.lower()].split('>')
		contractInputOfList =getElement(self.driver, locateType, locateExpression)
		return contractInputOfList
	def contractSearchOfList(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.contractSearchOfList'.lower()].split('>')
		contractSearchOfList =getElement(self.driver, locateType, locateExpression)
		return contractSearchOfList
	def contractSearchResultOfList(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.contractSearchResultOfList'.lower()].split('>')
		contractSearchResultOfList =getElement(self.driver, locateType, locateExpression)
		return contractSearchResultOfList
	def collectionTypeBoxOfList(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.collectionTypeBoxOfList'.lower()].split('>')
		collectionTypeBoxOfList =getElement(self.driver, locateType, locateExpression)
		return collectionTypeBoxOfList
	def collectionTypeOfList(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.collectionTypeOfList'.lower()].split('>')
		collectionTypeOfList =getElement(self.driver, locateType, locateExpression)
		return collectionTypeOfList
	def search(self):
		locateType, locateExpression = self.addCollectionItems['addCollection.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search