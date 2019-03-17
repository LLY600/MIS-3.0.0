'''
保证金处理确认页面
'''
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback
from Action.login import *

class MarginHandleConfirmPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.readConfigurationFile = readConfigurationFile()
		self.marginHandleConfirm = self.readConfigurationFile.getItemSection('marginHandleConfirm')
	def financialManagement(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.financialManagement'.lower()].split('>')
		financialManagement = getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def marginManagement(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.marginManagement'.lower()].split('>')
		financialManagement = getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def marginHandleConfirmMenu(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.marginHandleConfirm'.lower()].split('>')
		marginHandleConfirm = getElement(self.driver, locateType, locateExpression)
		return marginHandleConfirm
	def frameOfMarginHandleConfirm(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.frameOfMarginHandleConfirm'.lower()].split('>')
		frameOfMarginHandleConfirm = getElement(self.driver, locateType, locateExpression)
		return frameOfMarginHandleConfirm
	def contractName(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.contractName'.lower()].split('>')
		contractName = getElement(self.driver, locateType, locateExpression)
		return contractName
	def contractNameInput(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.contractNameInput'.lower()].split('>')
		contractNameInput = getElement(self.driver, locateType, locateExpression)
		return contractNameInput
	def search(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.search'.lower()].split('>')
		search = getElement(self.driver, locateType, locateExpression)
		return search
	def contactResult(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.contactResult'.lower()].split('>')
		contactResult = getElement(self.driver, locateType, locateExpression)
		return contactResult
	def searchBox(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.searchBox'.lower()].split('>')
		searchBox = getElement(self.driver, locateType, locateExpression)
		return searchBox
	def select(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.select'.lower()].split('>')
		select = getElement(self.driver, locateType, locateExpression)
		return select
	def confirm(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.confirm'.lower()].split('>')
		confirm = getElement(self.driver, locateType, locateExpression)
		return confirm
	def infomationConfirm(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.infomationConfirm'.lower()].split('>')
		infomationConfirm = getElement(self.driver, locateType, locateExpression)
		return infomationConfirm
	def information(self):
		locateType, locateExpression = self.marginHandleConfirm['marginHandleConfirm.information'.lower()].split('>')
		information = getElement(self.driver, locateType, locateExpression)
		return information.text

if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get('http://192.168.1.136:7009/')
	login(driver, 'LLY01', '123456')
	mhc = MarginHandleConfirmPage(driver)
	mhc.financialManagement().click()
	mhc.marginManagement().click()
	mhc.marginHandleConfirm().click()
	driver.switch_to.frame(mhc.frameOfMarginHandleConfirm())
	mhc.contractName().click()
	mhc.contractNameInput().send_keys('XCSD180921006')
	mhc.search().click()
	mhc.select().click()
	mhc.confirm().click()
	mhc.infomationConfirm().click()