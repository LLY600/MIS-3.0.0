'''
账单调整页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class BillAdjustPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.billAdjustItems = self.readConfigurationFile.getItemSection('billAdjust')
	def financialManagement(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.financialManagement'.lower()].split('>')
		financialManagement =getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def billAdjust(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.billAdjust'.lower()].split('>')
		billAdjust =getElement(self.driver, locateType, locateExpression)
		return billAdjust
	def billAdjustMaintain(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.billAdjustMaintain'.lower()].split('>')
		billAdjustMaintain =getElement(self.driver, locateType, locateExpression)
		return billAdjustMaintain
	def frameOfBillAdjust(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.frameOfBillAdjust'.lower()].split('>')
		frameOfBillAdjust =getElement(self.driver, locateType, locateExpression)
		return frameOfBillAdjust
	def add(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddBillAdjust(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.frameOfAddBillAdjust'.lower()].split('>')
		frameOfAddBillAdjust =getElement(self.driver, locateType, locateExpression)
		return frameOfAddBillAdjust
	def mall(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.mall'.lower()].split('>')
		mall =getElement(self.driver, locateType, locateExpression)
		return mall
	def mallSelect(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.mallSelect'.lower()].split('>')
		mallSelect =getElement(self.driver, locateType, locateExpression)
		return mallSelect
	def merchant(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.merchant'.lower()].split('>')
		merchant =getElement(self.driver, locateType, locateExpression)
		return merchant
	def merchantInput(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.merchantInput'.lower()].split('>')
		merchantInput =getElement(self.driver, locateType, locateExpression)
		return merchantInput
	def merchantSearch(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.merchantSearch'.lower()].split('>')
		merchantSearch =getElement(self.driver, locateType, locateExpression)
		return merchantSearch
	def merchantSearchResult(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.merchantSearchResult'.lower()].split('>')
		merchantSearchResult =getElement(self.driver, locateType, locateExpression)
		return merchantSearchResult
	def contract(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.contract'.lower()].split('>')
		contract =getElement(self.driver, locateType, locateExpression)
		return contract
	def contractInput(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.contractInput'.lower()].split('>')
		contractInput =getElement(self.driver, locateType, locateExpression)
		return contractInput
	def contractSearch(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.contractSearch'.lower()].split('>')
		contractSearch =getElement(self.driver, locateType, locateExpression)
		return contractSearch
	def contractSearchResult(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.contractSearchResult'.lower()].split('>')
		contractSearchResult =getElement(self.driver, locateType, locateExpression)
		return contractSearchResult
	def settlementGroup(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.settlementGroup'.lower()].split('>')
		settlementGroup =getElement(self.driver, locateType, locateExpression)
		return settlementGroup
	def settlementGroupSelect(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.settlementGroupSelect'.lower()].split('>')
		settlementGroupSelect =getElement(self.driver, locateType, locateExpression)
		return settlementGroupSelect
	def billNo(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.billNum'.lower()].split('>')
		billNo =getElement(self.driver, locateType, locateExpression)
		return billNo
	def billNoInput(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.billNumInput'.lower()].split('>')
		billNoInput =getElement(self.driver, locateType, locateExpression)
		return billNoInput
	def billNoSearch(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.billNumSearch'.lower()].split('>')
		billNoSearch =getElement(self.driver, locateType, locateExpression)
		return billNoSearch
	def billNoSearchResult(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.billNumSearchResult'.lower()].split('>')
		billNoSearchResult =getElement(self.driver, locateType, locateExpression)
		return billNoSearchResult
	def addAdjust(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.addAdjust'.lower()].split('>')
		addAdjust =getElement(self.driver, locateType, locateExpression)
		return addAdjust
	def costItemBox(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.costItemBox'.lower()].split('>')
		costItemBox =getElement(self.driver, locateType, locateExpression)
		return costItemBox
	def costItemInner(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.costItemInner'.lower()].split('>')
		costItemInner =getElement(self.driver, locateType, locateExpression)
		return costItemInner
	def costItem(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.costItem'.lower()].split('>')
		costItem =getElement(self.driver, locateType, locateExpression)
		return costItem
	def adjustMonthBox(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.adjustMonthBox'.lower()].split('>')
		adjustMonthBox =getElement(self.driver, locateType, locateExpression)
		return adjustMonthBox
	def adjustMonthInner(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.adjustMonthInner'.lower()].split('>')
		adjustMonthInner =getElement(self.driver, locateType, locateExpression)
		return adjustMonthInner
	def adjustMonth(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.adjustMonth'.lower()].split('>')
		adjustMonth =getElement(self.driver, locateType, locateExpression)
		return adjustMonth
	def adjustTypeBox(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.adjustTypeBox'.lower()].split('>')
		adjustTypeBox =getElement(self.driver, locateType, locateExpression)
		return adjustTypeBox
	def adjustTypeInner(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.adjustTypeInner'.lower()].split('>')
		adjustTypeInner =getElement(self.driver, locateType, locateExpression)
		return adjustTypeInner
	def adjustType(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.adjustType'.lower()].split('>')
		adjustType =getElement(self.driver, locateType, locateExpression)
		return adjustType
	def adjustMoneyBox(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.adjustMoneyBox'.lower()].split('>')
		adjustMoneyBox =getElement(self.driver, locateType, locateExpression)
		return adjustMoneyBox
	def adjustMoney(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.adjustMoney'.lower()].split('>')
		adjustMoney =getElement(self.driver, locateType, locateExpression)
		return adjustMoney
	def addButton(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.addButton'.lower()].split('>')
		addButton =getElement(self.driver, locateType, locateExpression)
		return addButton
	def information(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
	def informationConfirm(self):
		locateType, locateExpression = self.billAdjustItems['billAdjust.informationConfirm'.lower()].split('>')
		informationConfirm =getElement(self.driver, locateType, locateExpression)
		return informationConfirm