'''
添加单元页面对象
'''


from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class AddCellPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.addCellItems = self.readConfigurationFile.getItemSection('AddCell')
	def tenancyManagement(self):
		locateType, locateExpression = self.addCellItems['AddCell.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def propertyManagement(self):
		locateType, locateExpression = self.addCellItems['AddCell.propertyManagement'.lower()].split('>')
		propertyManagement =getElement(self.driver, locateType, locateExpression)
		return propertyManagement
	def cellManagement(self):
		locateType, locateExpression = self.addCellItems['AddCell.cellManagement'.lower()].split('>')
		cellManagement =getElement(self.driver, locateType, locateExpression)
		return cellManagement
	def frameOfCellManagement(self):
		locateType, locateExpression = self.addCellItems['AddCell.frameOfCellManagement'.lower()].split('>')
		frameOfCellManagement =getElement(self.driver, locateType, locateExpression)
		return frameOfCellManagement
	def add(self):
		locateType, locateExpression = self.addCellItems['AddCell.add'.lower()].split('>')
		add =getElement(self.driver, locateType, locateExpression)
		return add
	def frameOfAddCell(self):
		locateType, locateExpression = self.addCellItems['AddCell.frameOfAddCell'.lower()].split('>')
		frameOfAddCell =getElement(self.driver, locateType, locateExpression)
		return frameOfAddCell
	def cellNumBox(self):
		locateType, locateExpression = self.addCellItems['AddCell.cellNumBox'.lower()].split('>')
		cellNumBox =getElement(self.driver, locateType, locateExpression)
		return cellNumBox
	def cellNumInput(self):
		locateType, locateExpression = self.addCellItems['AddCell.cellNumInput'.lower()].split('>')
		cellNumInput =getElement(self.driver, locateType, locateExpression)
		return cellNumInput
	def mallBox(self):
		locateType, locateExpression = self.addCellItems['AddCell.mallBox'.lower()].split('>')
		mallBox =getElement(self.driver, locateType, locateExpression)
		return mallBox
	def mall(self):
		locateType, locateExpression = self.addCellItems['AddCell.mall'.lower()].split('>')
		mall = getElement(self.driver, locateType, locateExpression)
		return mall
	def mallSelect(self):
		locateType, locateExpression = self.addCellItems['AddCell.mallSelect'.lower()].split('>')
		mallSelect = getElement(self.driver, locateType, locateExpression)
		return mallSelect
	def merchandisingBox(self):
		locateType, locateExpression = self.addCellItems['AddCell.merchandisingBox'.lower()].split('>')
		merchandisingBox =getElement(self.driver, locateType, locateExpression)
		return merchandisingBox
	def merchandising(self):
		locateType, locateExpression = self.addCellItems['AddCell.merchandising'.lower()].split('>')
		merchandising =getElement(self.driver, locateType, locateExpression)
		return merchandising
	def merchandisingSelect(self):
		locateType, locateExpression = self.addCellItems['AddCell.merchandisingSelect'.lower()].split('>')
		merchandisingSelect =getElement(self.driver, locateType, locateExpression)
		return merchandisingSelect
	def buildingBox(self):
		locateType, locateExpression = self.addCellItems['AddCell.buildingBox'.lower()].split('>')
		buildingBox =getElement(self.driver, locateType, locateExpression)
		return buildingBox
	def building(self):
		locateType, locateExpression = self.addCellItems['AddCell.building'.lower()].split('>')
		building =getElement(self.driver, locateType, locateExpression)
		return building
	def buildingSelect(self):
		locateType, locateExpression = self.addCellItems['AddCell.buildingSelect'.lower()].split('>')
		buildingSelect =getElement(self.driver, locateType, locateExpression)
		return buildingSelect
	def buildAreaBox(self):
		locateType, locateExpression = self.addCellItems['AddCell.buildAreaBox'.lower()].split('>')
		buildAreaBox =getElement(self.driver, locateType, locateExpression)
		return buildAreaBox
	def buildAreaInput(self):
		locateType, locateExpression = self.addCellItems['AddCell.buildAreaInput'.lower()].split('>')
		buildAreaInput =getElement(self.driver, locateType, locateExpression)
		return buildAreaInput
	def areaBox(self):
		locateType, locateExpression = self.addCellItems['AddCell.areaBox'.lower()].split('>')
		areaBox =getElement(self.driver, locateType, locateExpression)
		return areaBox
	def areaInput(self):
		locateType, locateExpression = self.addCellItems['AddCell.areaInput'.lower()].split('>')
		areaInput =getElement(self.driver, locateType, locateExpression)
		return areaInput
	def cellDescriptionBox(self):
		locateType, locateExpression = self.addCellItems['AddCell.cellDescriptionBox'.lower()].split('>')
		cellDescriptionBox =getElement(self.driver, locateType, locateExpression)
		return cellDescriptionBox
	def cellDescriptionInput(self):
		locateType, locateExpression = self.addCellItems['AddCell.cellDescriptionInput'.lower()].split('>')
		cellDescriptionInput =getElement(self.driver, locateType, locateExpression)
		return cellDescriptionInput
	def save(self):
		locateType, locateExpression = self.addCellItems['AddCell.save'.lower()].split('>')
		save =getElement(self.driver, locateType, locateExpression)
		return save
	def information(self):
		locateType, locateExpression = self.addCellItems['AddCell.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
	def confirm(self):
		locateType, locateExpression = self.addCellItems['AddCell.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def search(self):
		locateType, locateExpression = self.addCellItems['AddCell.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search