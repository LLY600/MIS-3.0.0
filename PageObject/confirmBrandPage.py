'''
添加品牌确认页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class ConfirmBrandPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.brandConfirmItems = self.readConfigurationFile.getItemSection('BrandConfirm')
	def tenancyManagement(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def investmentResourcesManagement(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.investmentResourcesManagement'.lower()].split('>')
		investmentResourcesManagement =getElement(self.driver, locateType, locateExpression)
		return investmentResourcesManagement
	def brandConfirm(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.brandConfirm'.lower()].split('>')
		brandConfirm =getElement(self.driver, locateType, locateExpression)
		return brandConfirm
	def frameOfBrandConfirm(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.frameOfBrandConfirm'.lower()].split('>')
		frameOfBrandConfirm =getElement(self.driver, locateType, locateExpression)
		return frameOfBrandConfirm
	def brandBox(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.brandBox'.lower()].split('>')
		brandBox =getElement(self.driver, locateType, locateExpression)
		return brandBox
	def brand(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.brand'.lower()].split('>')
		brand =getElement(self.driver, locateType, locateExpression)
		return brand
	def search(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search
	def select(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.brandSelect'.lower()].split('>')
		brandSelect =getElement(self.driver, locateType, locateExpression)
		return brandSelect
	def confirmButton(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.confirmButton'.lower()].split('>')
		confirmButton =getElement(self.driver, locateType, locateExpression)
		return confirmButton
	def confirm(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def information(self):
		locateType, locateExpression = self.brandConfirmItems['BrandConfirm.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text