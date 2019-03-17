'''
添加店铺信息页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddStorePage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addStoreItems = self.readConfigurationFile.getItemSection('addStore')
	def tenancyManagement(self):
		locateType, locateExpression = self.addStoreItems['addStore.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def investmentResourcesManagement(self):
		locateType, locateExpression = self.addStoreItems['addStore.investmentResourcesManagement'.lower()].split('>')
		investmentResourcesManagement =getElement(self.driver, locateType, locateExpression)
		return investmentResourcesManagement
	def storeManagement(self):
		locateType, locateExpression = self.addStoreItems['addStore.storeManagement'.lower()].split('>')
		storeManagement =getElement(self.driver, locateType, locateExpression)
		return storeManagement
	def frameOfStoreManagement(self):
		locateType, locateExpression = self.addStoreItems['addStore.frameOfStoreManagement'.lower()].split('>')
		frameOfStoreManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfStoreManagement
	def add(self):
		locateType, locateExpression = self.addStoreItems['addStore.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddStore(self):
		locateType, locateExpression = self.addStoreItems['addStore.frameOfAddStore'.lower()].split('>')
		frameOfAddStore =getElement(self.driver, locateType, locateExpression)
		return frameOfAddStore
	def storeNumBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.storeNumBox'.lower()].split('>')
		storeNumBox =getElement(self.driver, locateType, locateExpression)
		return storeNumBox
	def storeNum(self):
		locateType, locateExpression = self.addStoreItems['addStore.storeNum'.lower()].split('>')
		storeNum =getElement(self.driver, locateType, locateExpression)
		return storeNum
	def storeNameBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.storeNameBox'.lower()].split('>')
		storeNameBox =getElement(self.driver, locateType, locateExpression)
		return storeNameBox
	def storeName(self):
		locateType, locateExpression = self.addStoreItems['addStore.storeName'.lower()].split('>')
		storeName =getElement(self.driver, locateType, locateExpression)
		return storeName
	def salesTypeBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.salesTypeBox'.lower()].split('>')
		salesTypeBox =getElement(self.driver, locateType, locateExpression)
		return salesTypeBox
	def salesType(self):
		locateType, locateExpression = self.addStoreItems['addStore.salesType'.lower()].split('>')
		salesType =getElement(self.driver, locateType, locateExpression)
		return salesType
	def salesTypeSelect(self):
		locateType, locateExpression = self.addStoreItems['addStore.salesTypeSelect'.lower()].split('>')
		salesTypeSelect =getElement(self.driver, locateType, locateExpression)
		return salesTypeSelect
	def mallNameBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.mallNameBox'.lower()].split('>')
		mallNameBox =getElement(self.driver, locateType, locateExpression)
		return mallNameBox
	def mallName(self):
		locateType, locateExpression = self.addStoreItems['addStore.mallName'.lower()].split('>')
		mallName =getElement(self.driver, locateType, locateExpression)
		return mallName
	def mallNameSelect(self):
		locateType, locateExpression = self.addStoreItems['addStore.mallNameSelect'.lower()].split('>')
		mallNameSelect =getElement(self.driver, locateType, locateExpression)
		return mallNameSelect
	def merchantBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.merchantBox'.lower()].split('>')
		merchantBox =getElement(self.driver, locateType, locateExpression)
		return merchantBox
	def merchant(self):
		locateType, locateExpression = self.addStoreItems['addStore.merchant'.lower()].split('>')
		merchant =getElement(self.driver, locateType, locateExpression)
		return merchant
	def merchantInputBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.merchantInputBox'.lower()].split('>')
		merchantInputBox =getElement(self.driver, locateType, locateExpression)
		return merchantInputBox
	def merchantInput(self):
		locateType, locateExpression = self.addStoreItems['addStore.merchantInput'.lower()].split('>')
		merchantInput =getElement(self.driver, locateType, locateExpression)
		return merchantInput
	def merchantSearch(self):
		locateType, locateExpression = self.addStoreItems['addStore.merchantSearch'.lower()].split('>')
		merchantSearch =getElement(self.driver, locateType, locateExpression)
		return merchantSearch
	def merchantSelect(self):
		locateType, locateExpression = self.addStoreItems['addStore.merchantSelect'.lower()].split('>')
		merchantSelect =getElement(self.driver, locateType, locateExpression)
		return merchantSelect
	def brandBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.brandBox'.lower()].split('>')
		brandBox =getElement(self.driver, locateType, locateExpression)
		return brandBox
	def brand(self):
		locateType, locateExpression = self.addStoreItems['addStore.brand'.lower()].split('>')
		brand =getElement(self.driver, locateType, locateExpression)
		return brand
	def brandInputBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.brandInputBox'.lower()].split('>')
		brandInputBox =getElement(self.driver, locateType, locateExpression)
		return brandInputBox
	def brandInput(self):
		locateType, locateExpression = self.addStoreItems['addStore.brandInput'.lower()].split('>')
		brandInput =getElement(self.driver, locateType, locateExpression)
		return brandInput
	def brandSearch(self):
		locateType, locateExpression = self.addStoreItems['addStore.brandSearch'.lower()].split('>')
		brandSearch =getElement(self.driver, locateType, locateExpression)
		return brandSearch
	def brandSelect(self):
		locateType, locateExpression = self.addStoreItems['addStore.brandSelect'.lower()].split('>')
		brandSelect =getElement(self.driver, locateType, locateExpression)
		return brandSelect
	def mainBrandBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.mainBrandBox'.lower()].split('>')
		mainBrandBox =getElement(self.driver, locateType, locateExpression)
		return mainBrandBox
	def mainBrand(self):
		locateType, locateExpression = self.addStoreItems['addStore.mainBrand'.lower()].split('>')
		mainBrand =getElement(self.driver, locateType, locateExpression)
		return mainBrand
	def mainBrandInputBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.mainBrandInputBox'.lower()].split('>')
		mainBrandInputBox =getElement(self.driver, locateType, locateExpression)
		return mainBrandInputBox
	def mainBrandInput(self):
		locateType, locateExpression = self.addStoreItems['addStore.mainBrandInput'.lower()].split('>')
		mainBrandInput =getElement(self.driver, locateType, locateExpression)
		return mainBrandInput
	def mainBrandSearch(self):
		locateType, locateExpression = self.addStoreItems['addStore.mainBrandSearch'.lower()].split('>')
		mainBrandSearch =getElement(self.driver, locateType, locateExpression)
		return mainBrandSearch
	def mainBrandSelect(self):
		locateType, locateExpression = self.addStoreItems['addStore.mainBrandSelect'.lower()].split('>')
		mainBrandSelect =getElement(self.driver, locateType, locateExpression)
		return mainBrandSelect
	def save(self):
		locateType, locateExpression = self.addStoreItems['addStore.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addStoreItems['addStore.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
	def confirm(self):
		locateType, locateExpression = self.addStoreItems['addStore.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def storeNameListBox(self):
		locateType, locateExpression = self.addStoreItems['addStore.storeNameListBox'.lower()].split('>')
		storeNameListBox =getElement(self.driver, locateType, locateExpression)
		return storeNameListBox
	def storeNameList(self):
		locateType, locateExpression = self.addStoreItems['addStore.storeNameList'.lower()].split('>')
		storeNameList =getElement(self.driver, locateType, locateExpression)
		return storeNameList
	def search(self):
		locateType, locateExpression = self.addStoreItems['addStore.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search