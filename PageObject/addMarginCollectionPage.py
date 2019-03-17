
'''
添加保证金收取页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *


class AddMarginCollectionPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.readConfigurationFile = readConfigurationFile()
		self.addMarginCollection = self.readConfigurationFile.getItemSection('addMarginCollection')
	def financialManagement(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.financialManagement'.lower()].split('>')
		financialManagement = getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def marginManagement(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.marginManagement'.lower()].split('>')
		marginManagement = getElement(self.driver, locateType, locateExpression)
		return marginManagement
	def marginCollection(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.marginCollection'.lower()].split('>')
		marginCollection = getElement(self.driver, locateType, locateExpression)
		return marginCollection
	def frameOfMarginCollection(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.frameOfMarginCollection'.lower()].split('>')
		frameOfMarginCollection = getElement(self.driver, locateType, locateExpression)
		return frameOfMarginCollection
	def add(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.add'.lower()].split('>')
		add = getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfaddMarginCollection(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.frameOfaddMarginCollection'.lower()].split('>')
		frameOfaddMarginCollection = getElement(self.driver, locateType, locateExpression)
		return frameOfaddMarginCollection
	def mallBox(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.mallBox'.lower()].split('>')
		mallBox = getElement(self.driver, locateType, locateExpression)
		return mallBox
	def mallName(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.mallName'.lower()].split('>')
		mallName = getElement(self.driver, locateType, locateExpression)
		return mallName
	def mallNameSelect(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.mallNameSelect'.lower()].split('>')
		mallNameSelect = getElement(self.driver, locateType, locateExpression)
		return mallNameSelect
	def merchantNameBox(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.merchantNameBox'.lower()].split('>')
		merchantNameBox = getElement(self.driver, locateType, locateExpression)
		return merchantNameBox
	def merchantName(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.merchantName'.lower()].split('>')
		merchantName = getElement(self.driver, locateType, locateExpression)
		return merchantName
	def merchantNameInputBox(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.merchantNameInputBox'.lower()].split('>')
		merchantNameInputBox = getElement(self.driver, locateType, locateExpression)
		return merchantNameInputBox
	def merchantNameInput(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.merchantNameInput'.lower()].split('>')
		merchantNameInput = getElement(self.driver, locateType, locateExpression)
		return merchantNameInput
	def merchantSearch(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.merchantSearch'.lower()].split('>')
		merchantSearch = getElement(self.driver, locateType, locateExpression)
		return merchantSearch
	def merchantSearchResult(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.merchantSearchResult'.lower()].split('>')
		merchantSearchResult = getElement(self.driver, locateType, locateExpression)
		return merchantSearchResult
	def contractNameBox(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.contractNameBox'.lower()].split('>')
		contractNameBox = getElement(self.driver, locateType, locateExpression)
		return contractNameBox
	def contractName(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.contractName'.lower()].split('>')
		contractName = getElement(self.driver, locateType, locateExpression)
		return contractName
	def contractNameInputBox(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.contractNameInputBox'.lower()].split('>')
		contractNameInputBox = getElement(self.driver, locateType, locateExpression)
		return contractNameInputBox
	def contractNameInput(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.contractNameInput'.lower()].split('>')
		contractNameInput = getElement(self.driver, locateType, locateExpression)
		return contractNameInput
	def contractSearch(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.contractSearch'.lower()].split('>')
		contractSearch = getElement(self.driver, locateType, locateExpression)
		return contractSearch
	def contractSearchResult(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.contractSearchResult'.lower()].split('>')
		contractSearchResult = getElement(self.driver, locateType, locateExpression)
		return contractSearchResult
	def paymentTimeBox(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentTimeBox'.lower()].split('>')
		paymentTimeBox = getElement(self.driver, locateType, locateExpression)
		return paymentTimeBox
	def paymentTime(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentTime'.lower()].split('>')
		paymentTime = getElement(self.driver, locateType, locateExpression)
		return paymentTime
	def addMargin(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.addMargin'.lower()].split('>')
		addMargin = getElement(self.driver, locateType, locateExpression)
		return addMargin
	def feeItemBox1(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItemBox1'.lower()].split('>')
		feeItemBox1 = getElement(self.driver, locateType, locateExpression)
		return feeItemBox1
	def feeItemBox2(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItemBox2'.lower()].split('>')
		feeItemBox2 = getElement(self.driver, locateType, locateExpression)
		return feeItemBox2
	def feeItemBox3(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItemBox3'.lower()].split('>')
		feeItemBox3 = getElement(self.driver, locateType, locateExpression)
		return feeItemBox3
	def feeItemBox4(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItemBox4'.lower()].split('>')
		feeItemBox4 = getElement(self.driver, locateType, locateExpression)
		return feeItemBox4
	def feeItemBox5(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItemBox5'.lower()].split('>')
		feeItemBox5 = getElement(self.driver, locateType, locateExpression)
		return feeItemBox5
	def feeItemBox6(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItemBox6'.lower()].split('>')
		feeItemBox6 = getElement(self.driver, locateType, locateExpression)
		return feeItemBox6
	def feeItem1(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItem1'.lower()].split('>')
		feeItem1 = getElement(self.driver, locateType, locateExpression)
		return feeItem1
	def feeItem2(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItem2'.lower()].split('>')
		feeItem2 = getElement(self.driver, locateType, locateExpression)
		return feeItem2
	def feeItem3(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItem3'.lower()].split('>')
		feeItem3 = getElement(self.driver, locateType, locateExpression)
		return feeItem3
	def feeItem4(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItem4'.lower()].split('>')
		feeItem4 = getElement(self.driver, locateType, locateExpression)
		return feeItem4
	def feeItem5(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItem5'.lower()].split('>')
		feeItem5 = getElement(self.driver, locateType, locateExpression)
		return feeItem5
	def feeItem6(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItem6'.lower()].split('>')
		feeItem6 = getElement(self.driver, locateType, locateExpression)
		return feeItem6
	def feeItemInputBox(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItemInputBox'.lower()].split('>')
		feeItemInputBox = getElement(self.driver, locateType, locateExpression)
		return feeItemInputBox
	def feeItemInput(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItemInput'.lower()].split('>')
		feeItemInput = getElement(self.driver, locateType, locateExpression)
		return feeItemInput
	def feeItemSearch(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItemSearch'.lower()].split('>')
		feeItemSearch = getElement(self.driver, locateType, locateExpression)
		return feeItemSearch
	def feeItemSearchResult(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.feeItemSearchResult'.lower()].split('>')
		feeItemSearchResult = getElement(self.driver, locateType, locateExpression)
		return feeItemSearchResult
	def currentPaymentMoneyBox1(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoneyBox1'.lower()].split('>')
		currentPaymentMoneyBox1 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoneyBox1
	def currentPaymentMoneyBox2(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoneyBox2'.lower()].split('>')
		currentPaymentMoneyBox2 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoneyBox2
	def currentPaymentMoneyBox3(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoneyBox3'.lower()].split('>')
		currentPaymentMoneyBox3 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoneyBox3
	def currentPaymentMoneyBox4(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoneyBox4'.lower()].split('>')
		currentPaymentMoneyBox4 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoneyBox4
	def currentPaymentMoneyBox5(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoneyBox5'.lower()].split('>')
		currentPaymentMoneyBox5 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoneyBox5
	def currentPaymentMoneyBox6(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoneyBox6'.lower()].split('>')
		currentPaymentMoneyBox6 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoneyBox6
	def currentPaymentMoney1(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoney1'.lower()].split('>')
		currentPaymentMoney1 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoney1
	def currentPaymentMoney2(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoney2'.lower()].split('>')
		currentPaymentMoney2 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoney2
	def currentPaymentMoney3(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoney3'.lower()].split('>')
		currentPaymentMoney3 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoney3
	def currentPaymentMoney4(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoney4'.lower()].split('>')
		currentPaymentMoney4 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoney4
	def currentPaymentMoney5(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoney5'.lower()].split('>')
		currentPaymentMoney5 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoney5
	def currentPaymentMoney6(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.currentPaymentMoney6'.lower()].split('>')
		currentPaymentMoney6 = getElement(self.driver, locateType, locateExpression)
		return currentPaymentMoney6
	def addRow(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.addRow'.lower()].split('>')
		addRow = getElement(self.driver, locateType, locateExpression)
		return addRow
	def paymentMethodBox1(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethodBox1'.lower()].split('>')
		paymentMethodBox1 = getElement(self.driver, locateType, locateExpression)
		return paymentMethodBox1
	def paymentMethodBox2(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethodBox2'.lower()].split('>')
		paymentMethodBox2 = getElement(self.driver, locateType, locateExpression)
		return paymentMethodBox2
	def paymentMethodBox3(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethodBox3'.lower()].split('>')
		paymentMethodBox3 = getElement(self.driver, locateType, locateExpression)
		return paymentMethodBox3
	def paymentMethodBox4(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethodBox4'.lower()].split('>')
		paymentMethodBox4 = getElement(self.driver, locateType, locateExpression)
		return paymentMethodBox4
	def paymentMethod1(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethod1'.lower()].split('>')
		paymentMethod1 = getElement(self.driver, locateType, locateExpression)
		return paymentMethod1
	def paymentMethod2(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethod2'.lower()].split('>')
		paymentMethod2 = getElement(self.driver, locateType, locateExpression)
		return paymentMethod2
	def paymentMethod3(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethod3'.lower()].split('>')
		paymentMethod3 = getElement(self.driver, locateType, locateExpression)
		return paymentMethod3
	def paymentMethod4(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethod4'.lower()].split('>')
		paymentMethod4 = getElement(self.driver, locateType, locateExpression)
		return paymentMethod4
	def paymentMethodSelect1(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethodSelect1'.lower()].split('>')
		paymentMethodSelect1 = getElement(self.driver, locateType, locateExpression)
		return paymentMethodSelect1
	def paymentMethodSelect2(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethodSelect2'.lower()].split('>')
		paymentMethodSelect2 = getElement(self.driver, locateType, locateExpression)
		return paymentMethodSelect2
	def paymentMethodSelect3(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethodSelect3'.lower()].split('>')
		paymentMethodSelect3 = getElement(self.driver, locateType, locateExpression)
		return paymentMethodSelect3
	def paymentMethodSelect4(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMethodSelect4'.lower()].split('>')
		paymentMethodSelect4 = getElement(self.driver, locateType, locateExpression)
		return paymentMethodSelect4
	def paymentMoneyBox1(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMoneyBox1'.lower()].split('>')
		paymentMoneyBox1 = getElement(self.driver, locateType, locateExpression)
		return paymentMoneyBox1
	def paymentMoneyBox2(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMoneyBox2'.lower()].split('>')
		paymentMoneyBox2 = getElement(self.driver, locateType, locateExpression)
		return paymentMoneyBox2
	def paymentMoneyBox3(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMoneyBox3'.lower()].split('>')
		paymentMoneyBox3 = getElement(self.driver, locateType, locateExpression)
		return paymentMoneyBox3
	def paymentMoneyBox4(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMoneyBox4'.lower()].split('>')
		paymentMoneyBox4 = getElement(self.driver, locateType, locateExpression)
		return paymentMoneyBox4
	def paymentMoney1(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMoney1'.lower()].split('>')
		paymentMoney1 = getElement(self.driver, locateType, locateExpression)
		return paymentMoney1
	def paymentMoney2(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMoney2'.lower()].split('>')
		paymentMoney2 = getElement(self.driver, locateType, locateExpression)
		return paymentMoney2
	def paymentMoney3(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMoney3'.lower()].split('>')
		paymentMoney3 = getElement(self.driver, locateType, locateExpression)
		return paymentMoney3
	def paymentMoney4(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.paymentMoney4'.lower()].split('>')
		paymentMoney4 = getElement(self.driver, locateType, locateExpression)
		return paymentMoney4
	def save(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.save'.lower()].split('>')
		save = getElement(self.driver, locateType, locateExpression)
		return save
	def confirm(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.confirm'.lower()].split('>')
		confirm = getElement(self.driver, locateType, locateExpression)
		return confirm
	def information(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.information'.lower()].split('>')
		information = getElement(self.driver, locateType, locateExpression)
		return information.text
	def close(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.close'.lower()].split('>')
		close = getElement(self.driver, locateType, locateExpression)
		return close
	def contract(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.contract'.lower()].split('>')
		contract = getElement(self.driver, locateType, locateExpression)
		return contract
	def contractSearch2(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.contractSearch2'.lower()].split('>')
		contractSearch2 = getElement(self.driver, locateType, locateExpression)
		return contractSearch2
	def contractSearch2Result(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.contractSearch2Result'.lower()].split('>')
		contractSearch2Result = getElement(self.driver, locateType, locateExpression)
		return contractSearch2Result
	def search(self):
		locateType, locateExpression = self.addMarginCollection['addMarginCollection.search'.lower()].split('>')
		search = getElement(self.driver, locateType, locateExpression)
		return search