'''
添加品牌页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddBrandPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addBrandItems = self.readConfigurationFile.getItemSection('AddBrand')
	def tenancyManagement(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def investmentResourcesManagement(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.investmentResourcesManagement'.lower()].split('>')
		investmentResourcesManagement =getElement(self.driver, locateType, locateExpression)
		return investmentResourcesManagement
	def brandManagement(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.brandManagement'.lower()].split('>')
		brandManagement =getElement(self.driver, locateType, locateExpression)
		return brandManagement
	def frameOfBrandManagement(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.frameOfBrandManagement'.lower()].split('>')
		frameOfBrandManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfBrandManagement
	def add(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddBrand(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.frameOfAddBrand'.lower()].split('>')
		frameOfAddBrand =getElement(self.driver, locateType, locateExpression)
		return frameOfAddBrand
	def brandNameBox(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.brandNameBox'.lower()].split('>')
		brandNameBox =getElement(self.driver, locateType, locateExpression)
		return brandNameBox
	def brandNumBox(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.brandNumBox'.lower()].split('>')
		brandNumBox =getElement(self.driver, locateType, locateExpression)
		return brandNumBox
	def brandNum(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.brandNum'.lower()].split('>')
		brandNum =getElement(self.driver, locateType, locateExpression)
		return brandNum
	def brandNameInput(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.brandNameInput'.lower()].split('>')
		brandNameInput =getElement(self.driver, locateType, locateExpression)
		return brandNameInput
	def merchandisingBox(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.merchandisingBox'.lower()].split('>')
		merchandisingBox =getElement(self.driver, locateType, locateExpression)
		return merchandisingBox
	def merchandising(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.merchandising'.lower()].split('>')
		merchandising =getElement(self.driver, locateType, locateExpression)
		return merchandising
	def merchandisingSelect(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.merchandisingSelect'.lower()].split('>')
		merchandisingSelect =getElement(self.driver, locateType, locateExpression)
		return merchandisingSelect
	def companyBox(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.companyBox'.lower()].split('>')
		companyBox =getElement(self.driver, locateType, locateExpression)
		return companyBox
	def company(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.company'.lower()].split('>')
		company =getElement(self.driver, locateType, locateExpression)
		return company
	def leaderBox(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.leaderBox'.lower()].split('>')
		leaderBox =getElement(self.driver, locateType, locateExpression)
		return leaderBox
	def leader(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.leader'.lower()].split('>')
		leader =getElement(self.driver, locateType, locateExpression)
		return leader
	def addressBox(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.addressBox'.lower()].split('>')
		addressBox =getElement(self.driver, locateType, locateExpression)
		return addressBox
	def address(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.address'.lower()].split('>')
		address =getElement(self.driver, locateType, locateExpression)
		return address
	def phoneBox(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.phoneBox'.lower()].split('>')
		phoneBox =getElement(self.driver, locateType, locateExpression)
		return phoneBox
	def phone(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.phone'.lower()].split('>')
		phone =getElement(self.driver, locateType, locateExpression)
		return phone
	def save(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
	def confirm(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def search(self):
		locateType, locateExpression = self.addBrandItems['AddBrand.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search