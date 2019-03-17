'''
添加货品组别页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddCommodityGroupPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addCommodityGroupItems = self.readConfigurationFile.getItemSection('addCommodityGroup')
	def tenancyManagement(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def investmentResourcesManagement(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.investmentResourcesManagement'.lower()].split('>')
		investmentResourcesManagement =getElement(self.driver, locateType, locateExpression)
		return investmentResourcesManagement
	def commodityGroupManagement(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.commodityGroupManagement'.lower()].split('>')
		commodityGroupManagement =getElement(self.driver, locateType, locateExpression)
		return commodityGroupManagement
	def frameOfCommodityGroupManagement(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.frameOfCommodityGroupManagement'.lower()].split('>')
		frameOfCommodityGroupManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfCommodityGroupManagement
	def add(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddCommodityGroup(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.frameOfAddCommodityGroup'.lower()].split('>')
		frameOfAddCommodityGroup =getElement(self.driver, locateType, locateExpression)
		return frameOfAddCommodityGroup
	def commodityGroupNumBox(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.commodityGroupNumBox'.lower()].split('>')
		commodityGroupNumBox =getElement(self.driver, locateType, locateExpression)
		return commodityGroupNumBox
	def commodityGroupNum(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.commodityGroupNum'.lower()].split('>')
		commodityGroupNum =getElement(self.driver, locateType, locateExpression)
		return commodityGroupNum
	def commodityGroupNameBox(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.commodityGroupNameBox'.lower()].split('>')
		commodityGroupNameBox =getElement(self.driver, locateType, locateExpression)
		return commodityGroupNameBox
	def commodityGroupName(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.commodityGroupName'.lower()].split('>')
		commodityGroupName =getElement(self.driver, locateType, locateExpression)
		return commodityGroupName
	def save(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addCommodityGroupItems['addCommodityGroup.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text