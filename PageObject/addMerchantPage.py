'''
添加商户页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddMerchantPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.readConfigurationFile = readConfigurationFile()
		self.addMerchantItem = self.readConfigurationFile.getItemSection('addMerchant')
	def tenancyManagement(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.tenancyManagement'.lower()].split('>')
		tenancyManagement = getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def investmentResourcesManagement(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.investmentResourcesManagement'.lower()].split('>')
		investmentResourcesManagement = getElement(self.driver, locateType, locateExpression)
		return investmentResourcesManagement
	def merchantManagement(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.merchantManagement'.lower()].split('>')
		merchantManagement = getElement(self.driver, locateType, locateExpression)
		return merchantManagement
	def frameOfMerchantManagement(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.frameOfMerchantManagement'.lower()].split('>')
		frameOfMerchantManagement = getElement(self.driver, locateType, locateExpression)
		return frameOfMerchantManagement
	def add(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.add'.lower()].split('>')
		add = getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddMerchant(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.frameOfAddMerchant'.lower()].split('>')
		frameOfAddMerchant = getElement(self.driver, locateType, locateExpression)
		return frameOfAddMerchant
	def mallNameBox(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.mallNameBox'.lower()].split('>')
		mallNameBox = getElement(self.driver, locateType, locateExpression)
		return mallNameBox
	def mallName(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.mallName'.lower()].split('>')
		mallName = getElement(self.driver, locateType, locateExpression)
		return mallName
	def mallNameSelect(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.mallNameSelect'.lower()].split('>')
		mallNameSelect = getElement(self.driver, locateType, locateExpression)
		return mallNameSelect
	def merchantNumBox(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.merchantNumBox'.lower()].split('>')
		merchantNumBox = getElement(self.driver, locateType, locateExpression)
		return merchantNumBox
	def merchantNum(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.merchantNum'.lower()].split('>')
		merchantNum = getElement(self.driver, locateType, locateExpression)
		return merchantNum
	def merchantNameBox(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.merchantNameBox'.lower()].split('>')
		merchantNameBox = getElement(self.driver, locateType, locateExpression)
		return merchantNameBox
	def merchantName(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.merchantName'.lower()].split('>')
		merchantName = getElement(self.driver, locateType, locateExpression)
		return merchantName
	def merchantPropertyBox(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.merchantPropertyBox'.lower()].split('>')
		merchantPropertyBox = getElement(self.driver, locateType, locateExpression)
		return merchantPropertyBox
	def merchantProperty(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.merchantProperty'.lower()].split('>')
		merchantProperty = getElement(self.driver, locateType, locateExpression)
		return merchantProperty
	def merchantPropertyOfValue(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.merchantPropertyOfValue'.lower()].split('>')
		merchantPropertyOfValue = getElement(self.driver, locateType, locateExpression)
		return merchantPropertyOfValue
	def save(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.save'.lower()].split('>')
		save = getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.information'.lower()].split('>')
		information = getElement(self.driver, locateType, locateExpression)
		return information.text
	def confirm(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.confirm'.lower()].split('>')
		confirm = getElement(self.driver, locateType, locateExpression)
		return confirm
	def merchant(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.merchant'.lower()].split('>')
		merchant = getElement(self.driver, locateType, locateExpression)
		return merchant
	def search(self):
		locateType, locateExpression = self.addMerchantItem['addMerchant.search'.lower()].split('>')
		search = getElement(self.driver, locateType, locateExpression)
		return search