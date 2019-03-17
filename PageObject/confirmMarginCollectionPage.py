'''
保证金收取确认页面
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class MarginCollectionConfirmPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.readConfigurationFile = readConfigurationFile()
		self.addMarginCollection = self.readConfigurationFile.getItemSection('marginCollectionConfirm')
	def financialManagement(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.financialManagement'.lower()].split('>')
		financialManagement = getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def marginManagement(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.marginManagement'.lower()].split('>')
		marginManagement = getElement(self.driver, locateType, locateExpression)
		return marginManagement
	def marginCollectionConfirm(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.marginCollectionConfirm'.lower()].split('>')
		marginCollectionConfirm = getElement(self.driver, locateType, locateExpression)
		return marginCollectionConfirm
	def frameOfCollectionConfirm(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.frameOfCollectionConfirm'.lower()].split('>')
		frameOfCollectionConfirm = getElement(self.driver, locateType, locateExpression)
		return frameOfCollectionConfirm
	def contractName(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.contractName'.lower()].split('>')
		contractName = getElement(self.driver, locateType, locateExpression)
		return contractName
	def contractNameInput(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.contractNameInput'.lower()].split('>')
		contractNameInput = getElement(self.driver, locateType, locateExpression)
		return contractNameInput
	def search(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.search'.lower()].split('>')
		search = getElement(self.driver, locateType, locateExpression)
		return search
	def contactResult(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.contactResult'.lower()].split('>')
		contactResult = getElement(self.driver, locateType, locateExpression)
		return contactResult
	def searchBox(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.searchBox'.lower()].split('>')
		searchBox = getElement(self.driver, locateType, locateExpression)
		return searchBox
	def select(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.select'.lower()].split('>')
		select = getElement(self.driver, locateType, locateExpression)
		return select
	def confirm(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.confirm'.lower()].split('>')
		confirm = getElement(self.driver, locateType, locateExpression)
		return confirm
	def infomationConfirm(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.infomationConfirm'.lower()].split('>')
		infomationConfirm = getElement(self.driver, locateType, locateExpression)
		return infomationConfirm
	def information(self):
		locateType, locateExpression = self.addMarginCollection['marginCollectionConfirm.information'.lower()].split('>')
		information = getElement(self.driver, locateType, locateExpression)
		return information.text
if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get('http://192.168.1.136:7009/')
	login(driver, 'LLY01', '123456')
	mcc = MarginCollectionConfirmPage(driver)
	mcc.financialManagement().click()
	mcc.marginManagement().click()
	mcc.marginCollectionConfirm().click()
	driver.switch_to.frame(mcc.frameOfCollectionConfirm())
	mcc.contractName().click()
	mcc.contractNameInput().send_keys('XCSD180921006')
	mcc.search().click()
	mcc.select().click()
	mcc.confirm().click()
	mcc.infomationConfirm().click()

