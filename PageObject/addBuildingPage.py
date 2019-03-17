'''
添加楼宇页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddBuildingPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addBuildingItems = self.readConfigurationFile.getItemSection('addBuilding')
	def tenancyManagement(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def propertyManagement(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.propertyManagement'.lower()].split('>')
		propertyManagement =getElement(self.driver, locateType, locateExpression)
		return propertyManagement
	def buildingManagement(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.buildingManagement'.lower()].split('>')
		buildingManagement =getElement(self.driver, locateType, locateExpression)
		return buildingManagement
	def frameOfBuildingManagement(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.frameOfBuildingManagement'.lower()].split('>')
		frameOfBuildingManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfBuildingManagement
	def selectMall(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.selectMall'.lower()].split('>')
		selectMall =getElement(self.driver, locateType, locateExpression)
		return selectMall
	def add(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddBuilding(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.frameOfAddBuilding'.lower()].split('>')
		frameOfAddBuilding =getElement(self.driver, locateType, locateExpression)
		return frameOfAddBuilding
	def buildingNumBox(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.buildingNumBox'.lower()].split('>')
		buildingNumBox =getElement(self.driver, locateType, locateExpression)
		return buildingNumBox
	def buildingNum(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.buildingNum'.lower()].split('>')
		buildingNum =getElement(self.driver, locateType, locateExpression)
		return buildingNum
	def buildingNameBox(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.buildingNameBox'.lower()].split('>')
		buildingNameBox =getElement(self.driver, locateType, locateExpression)
		return buildingNameBox
	def buildingName(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.buildingName'.lower()].split('>')
		buildingName =getElement(self.driver, locateType, locateExpression)
		return buildingName
	def buildingType(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.buildingType'.lower()].split('>')
		buildingType =getElement(self.driver, locateType, locateExpression)
		return buildingType
	def buildingTypeBox(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.buildingTypeBox'.lower()].split('>')
		buildingTypeBox =getElement(self.driver, locateType, locateExpression)
		return buildingTypeBox
	def buildingTypeSelect(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.buildingTypeSelect'.lower()].split('>')
		buildingTypeSelect =getElement(self.driver, locateType, locateExpression)
		return buildingTypeSelect
	def isBuildingBox(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.isBuildingBox'.lower()].split('>')
		isBuildingBox =getElement(self.driver, locateType, locateExpression)
		return isBuildingBox
	def isBuilding(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.isBuilding'.lower()].split('>')
		isBuilding =getElement(self.driver, locateType, locateExpression)
		return isBuilding
	def isBuildingSelect1(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.isBuildingSelect1'.lower()].split('>')
		isBuildingSelect1 =getElement(self.driver, locateType, locateExpression)
		return isBuildingSelect1
	def isBuildingSelect2(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.isBuildingSelect2'.lower()].split('>')
		isBuildingSelect2 =getElement(self.driver, locateType, locateExpression)
		return isBuildingSelect2
	def areaBox(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.areaBox'.lower()].split('>')
		areaBox =getElement(self.driver, locateType, locateExpression)
		return areaBox
	def area(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.area'.lower()].split('>')
		area =getElement(self.driver, locateType, locateExpression)
		return area
	def save(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addBuildingItems['addBuilding.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text