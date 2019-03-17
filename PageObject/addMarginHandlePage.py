'''
保证金处理页面
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class MarginHandlePage(object):
	def __init__(self, driver):
		self.driver = driver
		self.readConfigurationFile = readConfigurationFile()
		self.addMarginCollection = self.readConfigurationFile.getItemSection('marginHandle')
	def financialManagement(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.financialManagement'.lower()].split('>')
		financialManagement = getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def marginManagement(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.marginManagement'.lower()].split('>')
		marginManagement = getElement(self.driver, locateType, locateExpression)
		return marginManagement
	def marginHandle(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.marginHandle'.lower()].split('>')
		marginHandle = getElement(self.driver, locateType, locateExpression)
		return marginHandle
	def frameOfMarginHandle(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.frameOfMarginHandle'.lower()].split('>')
		frameOfMarginHandle = getElement(self.driver, locateType, locateExpression)
		return frameOfMarginHandle
	def add(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.add'.lower()].split('>')
		add = getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddMarginHandle(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.frameOfAddMarginHandle'.lower()].split('>')
		frameOfAddMarginHandle = getElement(self.driver, locateType, locateExpression)
		return frameOfAddMarginHandle
	def mall(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.mall'.lower()].split('>')
		mall = getElement(self.driver, locateType, locateExpression)
		return mall
	def mallSelect(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.mallSelect'.lower()].split('>')
		mallSelect = getElement(self.driver, locateType, locateExpression)
		return mallSelect
	def merchantName(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.merchantName'.lower()].split('>')
		merchantName = getElement(self.driver, locateType, locateExpression)
		return merchantName
	def merchantNameInput(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.merchantNameInput'.lower()].split('>')
		merchantNameInput = getElement(self.driver, locateType, locateExpression)
		return merchantNameInput
	def merchantNameSearch(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.merchantNameSearch'.lower()].split('>')
		merchantNameSearch = getElement(self.driver, locateType, locateExpression)
		return merchantNameSearch
	def merchantNameResult(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.merchantNameResult'.lower()].split('>')
		merchantNameResult = getElement(self.driver, locateType, locateExpression)
		return merchantNameResult
	def contractName(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.contractName'.lower()].split('>')
		contractName = getElement(self.driver, locateType, locateExpression)
		return contractName
	def contractNameInput(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.contractNameInput'.lower()].split('>')
		contractNameInput = getElement(self.driver, locateType, locateExpression)
		return contractNameInput
	def contractNameSearch(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.contractNameSearch'.lower()].split('>')
		contractNameSearch = getElement(self.driver, locateType, locateExpression)
		return contractNameSearch
	def contractNameResult(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.contractNameResult'.lower()].split('>')
		contractNameResult = getElement(self.driver, locateType, locateExpression)
		return contractNameResult
	def handleType(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.handleType'.lower()].split('>')
		handleType = getElement(self.driver, locateType, locateExpression)
		return handleType
	def handleTypeSelect(self, type):
		locateType, locateExpression = self.addMarginCollection[('marginHandle.handleType' + type).lower()].split('>')
		handleType = getElement(self.driver, locateType, locateExpression)
		return handleType
	def settlementGroupBox(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.settlementGroupBox'.lower()].split('>')
		settlementGroupBox = getElement(self.driver, locateType, locateExpression)
		return settlementGroupBox
	def settlementGroupInput(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.settlementGroupInput'.lower()].split('>')
		settlementGroupInput = getElement(self.driver, locateType, locateExpression)
		return settlementGroupInput
	def settlementGroupSearch(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.settlementGroupSearch'.lower()].split('>')
		settlementGroupSearch = getElement(self.driver, locateType, locateExpression)
		return settlementGroupSearch
	def settlementGroupResult(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.settlementGroupResult'.lower()].split('>')
		settlementGroupResult = getElement(self.driver, locateType, locateExpression)
		return settlementGroupResult
	def expenseItem(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.expenseItem'.lower()].split('>')
		expenseItem = getElement(self.driver, locateType, locateExpression)
		return expenseItem
	def expenseItemInput(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.expenseItemInput'.lower()].split('>')
		expenseItemInput = getElement(self.driver, locateType, locateExpression)
		return expenseItemInput
	def expenseItemSearch(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.expenseItemSearch'.lower()].split('>')
		expenseItemSearch = getElement(self.driver, locateType, locateExpression)
		return expenseItemSearch
	def expenseItemSelect(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.expenseItemSelect'.lower()].split('>')
		expenseItemSelect = getElement(self.driver, locateType, locateExpression)
		return expenseItemSelect
	def handleDate(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.handleDate'.lower()].split('>')
		handleDate = getElement(self.driver, locateType, locateExpression)
		return handleDate
	def handleDateInput(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.handleDateInput'.lower()].split('>')
		handleDateInput = getElement(self.driver, locateType, locateExpression)
		return handleDateInput
	def toAdvancePayment(self, row):
		locateType, locateExpression = self.addMarginCollection[('marginHandle.toAdvancePayment' + row).lower()].split('>')
		toAdvancePayment = getElement(self.driver, locateType, locateExpression)
		return toAdvancePayment
	def toConfiscatePayment(self, row):
		locateType, locateExpression = self.addMarginCollection[('marginHandle.toConfiscatePayment' + row).lower()].split('>')
		toConfiscatePayment = getElement(self.driver, locateType, locateExpression)
		return toConfiscatePayment
	def toReturnPayment(self, row):
		locateType, locateExpression = self.addMarginCollection[('marginHandle.toReturnPayment' + row).lower()].split('>')
		toReturnPayment = getElement(self.driver, locateType, locateExpression)
		return toReturnPayment
	def toAdvancePaymentInput(self, row):
		locateType, locateExpression = self.addMarginCollection[('marginHandle.toAdvancePaymentInput' + row).lower()].split('>')
		toAdvancePaymentInput = getElement(self.driver, locateType, locateExpression)
		return toAdvancePaymentInput
	def toConfiscatePaymentInput(self, row):
		locateType, locateExpression = self.addMarginCollection[('marginHandle.toConfiscatePaymentInput' + row).lower()].split('>')
		toConfiscatePaymentInput = getElement(self.driver, locateType, locateExpression)
		return toConfiscatePaymentInput
	def toReturnPaymentInput(self, row):
		locateType, locateExpression = self.addMarginCollection[('marginHandle.toReturnPaymentInput' + row).lower()].split('>')
		toReturnPaymentInput = getElement(self.driver, locateType, locateExpression)
		return toReturnPaymentInput
	def addRow(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.addRow'.lower()].split('>')
		addRow = getElement(self.driver, locateType, locateExpression)
		return addRow
	def paymentMethodBox(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.paymentMethodBox'.lower()].split('>')
		paymentMethodBox = getElement(self.driver, locateType, locateExpression)
		return paymentMethodBox
	def paymentMethodInput(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.paymentMethodInput'.lower()].split('>')
		paymentMethodInput = getElement(self.driver, locateType, locateExpression)
		return paymentMethodInput
	def paymentMethod(self, type):
		locateType, locateExpression = self.addMarginCollection[('marginHandle.paymentMethod' + type).lower()].split('>')
		paymentMethod = getElement(self.driver, locateType, locateExpression)
		return paymentMethod
	def paymentBox(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.paymentBox'.lower()].split('>')
		paymentBox = getElement(self.driver, locateType, locateExpression)
		return paymentBox
	def paymentInput(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.paymentInput'.lower()].split('>')
		paymentInput = getElement(self.driver, locateType, locateExpression)
		return paymentInput
	def save(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.save'.lower()].split('>')
		save = getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.information'.lower()].split('>')
		information = getElement(self.driver, locateType, locateExpression)
		return information.text
	def confirm(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.confirm'.lower()].split('>')
		confirm = getElement(self.driver, locateType, locateExpression)
		return confirm
	def contractNameInput1(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.contractNameInput1'.lower()].split('>')
		contractNameInput1 = getElement(self.driver, locateType, locateExpression)
		return contractNameInput1
	def contractNameSearch1(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.contractNameSearch1'.lower()].split('>')
		contractNameSearch1 = getElement(self.driver, locateType, locateExpression)
		return contractNameSearch1
	def contractNameResult1(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.contractNameResult1'.lower()].split('>')
		contractNameResult1 = getElement(self.driver, locateType, locateExpression)
		return contractNameResult1
	def handleType2(self, type):
		locateType, locateExpression = self.addMarginCollection[('marginHandle.handleType2' + type).lower()].split('>')
		handleType2 = getElement(self.driver, locateType, locateExpression)
		return handleType2
	def search(self):
		locateType, locateExpression = self.addMarginCollection['marginHandle.search'.lower()].split('>')
		search = getElement(self.driver, locateType, locateExpression)
		return search