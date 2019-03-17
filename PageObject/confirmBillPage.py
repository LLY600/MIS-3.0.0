'''
账单确认页面对象
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class BillConfirmPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.billConfirmItems = self.readConfigurationFile.getItemSection('billConfirm')
	def financialManagement(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.financialManagement'.lower()].split('>')
		financialManagement =getElement(self.driver, locateType, locateExpression)
		return financialManagement
	def billManagement(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.billManagement'.lower()].split('>')
		billManagement =getElement(self.driver, locateType, locateExpression)
		return billManagement
	def billConfirm(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.billConfirm'.lower()].split('>')
		billConfirm =getElement(self.driver, locateType, locateExpression)
		return billConfirm
	def frameOfBillConfirm(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.frameOfBillConfirm'.lower()].split('>')
		frameOfBillConfirm =getElement(self.driver, locateType, locateExpression)
		return frameOfBillConfirm
	def contractNameInput(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.contractNameInput'.lower()].split('>')
		contractNameInput =getElement(self.driver, locateType, locateExpression)
		return contractNameInput
	def search(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search
	def select(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.select'.lower()].split('>')
		select =getElement(self.driver, locateType, locateExpression)
		return select
	def confirmButton(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.confirmButton'.lower()].split('>')
		confirmButton =getElement(self.driver, locateType, locateExpression)
		return confirmButton
	def Confirm(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.Confirm'.lower()].split('>')
		Confirm =getElement(self.driver, locateType, locateExpression)
		return Confirm
	def information(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
	def informationConfirm(self):
		locateType, locateExpression = self.billConfirmItems['billConfirm.informationConfirm'.lower()].split('>')
		informationConfirm =getElement(self.driver, locateType, locateExpression)
		return informationConfirm