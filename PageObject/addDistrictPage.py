'''
添加区域页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddDistrictPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addDistrictItems = self.readConfigurationFile.getItemSection('addDistrict')
	def tenancyManagement(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def propertyManagement(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.propertyManagement'.lower()].split('>')
		propertyManagement =getElement(self.driver, locateType, locateExpression)
		return propertyManagement
	def districtManagement(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.districtManagement'.lower()].split('>')
		districtManagement =getElement(self.driver, locateType, locateExpression)
		return districtManagement
	def frameOfDistrictManagement(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.frameOfDistrictManagement'.lower()].split('>')
		frameOfDistrictManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfDistrictManagement
	def add(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddDistrictManagement(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.frameOfAddDistrictManagement'.lower()].split('>')
		frameOfAddDistrictManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfAddDistrictManagement
	def districtNum(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.districtNum'.lower()].split('>')
		districtNum =getElement(self.driver, locateType, locateExpression)
		return districtNum
	def districtName(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.districtName'.lower()].split('>')
		districtName =getElement(self.driver, locateType, locateExpression)
		return districtName
	def districtEName(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.districtEName'.lower()].split('>')
		districtEName =getElement(self.driver, locateType, locateExpression)
		return districtEName
	def save(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addDistrictItems['addDistrict.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text