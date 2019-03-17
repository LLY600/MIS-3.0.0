'''
添加费用项目页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddExpenseItemPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addExpenseItems = self.readConfigurationFile.getItemSection('addExpenseItem')
	def tenancyManagement(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.financialManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def basicSetting(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.basicSetting'.lower()].split('>')
		basicSetting =getElement(self.driver, locateType, locateExpression)
		return basicSetting
	def expenseItemManagement(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseItemManagement'.lower()].split('>')
		expenseItemManagement =getElement(self.driver, locateType, locateExpression)
		return expenseItemManagement
	def frameOfExpenseItemManagement(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.frameOfExpenseItemManagement'.lower()].split('>')
		frameOfExpenseItemManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfExpenseItemManagement
	def add(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddExpenseItem(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.frameOfAddExpenseItem'.lower()].split('>')
		frameOfAddExpenseItem =getElement(self.driver, locateType, locateExpression)
		return frameOfAddExpenseItem
	def expenseItemNumBox(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseItemNumBox'.lower()].split('>')
		expenseItemNumBox =getElement(self.driver, locateType, locateExpression)
		return expenseItemNumBox
	def expenseItemNum(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseItemNum'.lower()].split('>')
		expenseItemNum =getElement(self.driver, locateType, locateExpression)
		return expenseItemNum
	def expenseItemNameBox(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseItemNameBox'.lower()].split('>')
		expenseItemNameBox =getElement(self.driver, locateType, locateExpression)
		return expenseItemNameBox
	def expenseItemName(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseItemName'.lower()].split('>')
		expenseItemName =getElement(self.driver, locateType, locateExpression)
		return expenseItemName
	def settlementGroupNameBox(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.settlementGroupNameBox'.lower()].split('>')
		settlementGroupNameBox =getElement(self.driver, locateType, locateExpression)
		return settlementGroupNameBox
	def settlementGroupName(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.settlementGroupName'.lower()].split('>')
		settlementGroupName =getElement(self.driver, locateType, locateExpression)
		return settlementGroupName
	def settlementGroupNameSelect1(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.settlementGroupNameSelect1'.lower()].split('>')
		settlementGroupNameSelect1 =getElement(self.driver, locateType, locateExpression)
		return settlementGroupNameSelect1
	def settlementGroupNameSelect2(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.settlementGroupNameSelect2'.lower()].split('>')
		settlementGroupNameSelect2 =getElement(self.driver, locateType, locateExpression)
		return settlementGroupNameSelect2
	def expenseTypeBox(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseTypeBox'.lower()].split('>')
		expenseTypeBox =getElement(self.driver, locateType, locateExpression)
		return expenseTypeBox
	def expenseType(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseType'.lower()].split('>')
		expenseType =getElement(self.driver, locateType, locateExpression)
		return expenseType
	def expenseTypeSelect1(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseTypeSelect1'.lower()].split('>')
		expenseTypeSelect1 =getElement(self.driver, locateType, locateExpression)
		return expenseTypeSelect1
	def expenseTypeSelect2(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseTypeSelect2'.lower()].split('>')
		expenseTypeSelect2 =getElement(self.driver, locateType, locateExpression)
		return expenseTypeSelect2
	def expenseTypeSelect3(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseTypeSelect3'.lower()].split('>')
		expenseTypeSelect3 =getElement(self.driver, locateType, locateExpression)
		return expenseTypeSelect3
	def expenseTypeSelect4(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseTypeSelect4'.lower()].split('>')
		expenseTypeSelect4 =getElement(self.driver, locateType, locateExpression)
		return expenseTypeSelect4
	def expenseTypeSelect5(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseTypeSelect5'.lower()].split('>')
		expenseTypeSelect5 =getElement(self.driver, locateType, locateExpression)
		return expenseTypeSelect5
	def expenseTypeSelect6(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.expenseTypeSelect6'.lower()].split('>')
		expenseTypeSelect6 =getElement(self.driver, locateType, locateExpression)
		return expenseTypeSelect6
	def save(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
	def confirm(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def search(self):
		locateType, locateExpression = self.addExpenseItems['addExpenseItem.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search