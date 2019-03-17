'''
确认单元页面对象
'''


from toolKit.readConfigurationFile import *
from toolKit.findElements import *


class ConfirmCellPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()
		self.confirmCellItems = self.readConfigurationFile.getItemSection('ConfirmCell')
	def tenancyManagement(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.tenancyManagement'.lower()].split('>')
		tenancyManagement =getElement(self.driver, locateType, locateExpression)
		return tenancyManagement
	def propertyManagement(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.propertyManagement'.lower()].split('>')
		propertyManagement =getElement(self.driver, locateType, locateExpression)
		return propertyManagement
	def cellConfirm(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.cellConfirm'.lower()].split('>')
		cellConfirm =getElement(self.driver, locateType, locateExpression)
		return cellConfirm
	def frameOfCellConfirm(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.frameOfCellConfirm'.lower()].split('>')
		frameOfCellConfirm =getElement(self.driver, locateType, locateExpression)
		return frameOfCellConfirm
	def cellNumBox(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.cellNumBox'.lower()].split('>')
		cellNumBox =getElement(self.driver, locateType, locateExpression)
		return cellNumBox
	def cellNum(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.cellNum'.lower()].split('>')
		cellNum =getElement(self.driver, locateType, locateExpression)
		return cellNum
	def search(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.search'.lower()].split('>')
		search =getElement(self.driver, locateType, locateExpression)
		return search
	def select(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.cellSelect'.lower()].split('>')
		Select =getElement(self.driver, locateType, locateExpression)
		return Select
	def confirmButton(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.confirmButton'.lower()].split('>')
		confirmButton =getElement(self.driver, locateType, locateExpression)
		return confirmButton
	def confirm(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.confirm'.lower()].split('>')
		confirm =getElement(self.driver, locateType, locateExpression)
		return confirm
	def information(self):
		locateType, locateExpression = self.confirmCellItems['ConfirmCell.information'.lower()].split('>')
		information =getElement(self.driver, locateType, locateExpression)
		return information.text
