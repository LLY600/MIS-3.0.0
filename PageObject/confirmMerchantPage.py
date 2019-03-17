'''
确认商户页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *


class ConfirmMerchantPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 8, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.confirmMerchantItems = self.readConfigurationFile.getItemSection('confirmMerchant')
	def tenancyManagement(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def investmentResourcesManagement(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.investmentResourcesManagement'.lower()].split('>')
		investmentResourcesManagement =getElement(self.driver, locateType, locateExpression)
		return investmentResourcesManagement
	def merchantConfirm(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.merchantConfirm'.lower()].split('>')
		merchantManagement =getElement(self.driver, locateType, locateExpression)
		return merchantManagement
	def frameOfMerchantConfirm(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.frameOfMerchantConfirm'.lower()].split('>')
		frameOfMerchantConfirm =getElement(self.driver, locateType, locateExpression)
		return frameOfMerchantConfirm
	def merchantBox(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.merchantBox'.lower()].split('>')
		merchantBox =getElement(self.driver, locateType, locateExpression)
		return merchantBox
	def merchant(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.merchant'.lower()].split('>')
		merchant =getElement(self.driver, locateType, locateExpression)
		return merchant
	def search(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search
	def select(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.select'.lower()].split('>')
		select =getElement(self.driver, locateType, locateExpression)
		return select
	def confirmButton(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.confirmButton'.lower()].split('>')
		confirmButton =getElement(self.driver, locateType, locateExpression)
		return confirmButton
	def confirm(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def information(self):
		locateType, locateExpression = self.confirmMerchantItems['confirmMerchant.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text