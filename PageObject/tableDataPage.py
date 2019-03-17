'''
封装获取列表数据
'''

from selenium import webdriver
from toolKit.readConfigurationFile import *
from toolKit.findElements import *




# 方法row后面第一个数字表示行，其他数字表示列
# 举例：row11（第1行第1列），row110(第1行第10列)
# 举例：row21（第2行第1列），row210(第2行第10列)

class GetTableData(object):
	def __init__(self, driver):
		self.driver = driver
		self.readConfigurationFile = readConfigurationFile()
		self.getTableData = self.readConfigurationFile.getItemSection('getTableData')

	def row11(self):
		locateType, locateExpression = self.getTableData['getTableData.row11'.lower()].split('>')
		row1 = getElement(self.driver, locateType, locateExpression)
		return row1.text
	def row21(self):
		locateType, locateExpression = self.getTableData['getTableData.row21'.lower()].split('>')
		row1 = getElement(self.driver, locateType, locateExpression)
		return row1.text
	def row31(self):
		locateType, locateExpression = self.getTableData['getTableData.row31'.lower()].split('>')
		row1 = getElement(self.driver, locateType, locateExpression)
		return row1.text

	def row12(self):
		locateType, locateExpression = self.getTableData['getTableData.row12'.lower()].split('>')
		row2 = getElement(self.driver, locateType, locateExpression)
		return row2.text
	def row22(self):
		locateType, locateExpression = self.getTableData['getTableData.row22'.lower()].split('>')
		row2 = getElement(self.driver, locateType, locateExpression)
		return row2.text
	def row32(self):
		locateType, locateExpression = self.getTableData['getTableData.row32'.lower()].split('>')
		row2 = getElement(self.driver, locateType, locateExpression)
		return row2.text

	def row13(self):
		locateType, locateExpression = self.getTableData['getTableData.row13'.lower()].split('>')
		row3 = getElement(self.driver, locateType, locateExpression)
		return row3.text
	def row23(self):
		locateType, locateExpression = self.getTableData['getTableData.row23'.lower()].split('>')
		row3 = getElement(self.driver, locateType, locateExpression)
		return row3.text
	def row33(self):
		locateType, locateExpression = self.getTableData['getTableData.row33'.lower()].split('>')
		row3 = getElement(self.driver, locateType, locateExpression)
		return row3.text

	def row14(self):
		locateType, locateExpression = self.getTableData['getTableData.row14'.lower()].split('>')
		row4 = getElement(self.driver, locateType, locateExpression)
		return row4.text
	def row24(self):
		locateType, locateExpression = self.getTableData['getTableData.row24'.lower()].split('>')
		row4 = getElement(self.driver, locateType, locateExpression)
		return row4.text
	def row34(self):
		locateType, locateExpression = self.getTableData['getTableData.row34'.lower()].split('>')
		row4 = getElement(self.driver, locateType, locateExpression)
		return row4.text

	def row15(self):
		locateType, locateExpression = self.getTableData['getTableData.row15'.lower()].split('>')
		row5 = getElement(self.driver, locateType, locateExpression)
		return row5.text
	def row25(self):
		locateType, locateExpression = self.getTableData['getTableData.row25'.lower()].split('>')
		row5 = getElement(self.driver, locateType, locateExpression)
		return row5.text
	def row35(self):
		locateType, locateExpression = self.getTableData['getTableData.row35'.lower()].split('>')
		row5 = getElement(self.driver, locateType, locateExpression)
		return row5.text

	def row16(self):
		locateType, locateExpression = self.getTableData['getTableData.row16'.lower()].split('>')
		row6 = getElement(self.driver, locateType, locateExpression)
		return row6.text
	def row26(self):
		locateType, locateExpression = self.getTableData['getTableData.row26'.lower()].split('>')
		row6 = getElement(self.driver, locateType, locateExpression)
		return row6.text
	def row36(self):
		locateType, locateExpression = self.getTableData['getTableData.row36'.lower()].split('>')
		row6 = getElement(self.driver, locateType, locateExpression)
		return row6.text

	def row17(self):
		locateType, locateExpression = self.getTableData['getTableData.row17'.lower()].split('>')
		row7 = getElement(self.driver, locateType, locateExpression)
		return row7.text
	def row27(self):
		locateType, locateExpression = self.getTableData['getTableData.row27'.lower()].split('>')
		row7 = getElement(self.driver, locateType, locateExpression)
		return row7.text
	def row37(self):
		locateType, locateExpression = self.getTableData['getTableData.row37'.lower()].split('>')
		row7 = getElement(self.driver, locateType, locateExpression)
		return row7.text

	def row18(self):
		locateType, locateExpression = self.getTableData['getTableData.row18'.lower()].split('>')
		row8 = getElement(self.driver, locateType, locateExpression)
		return row8.text
	def row28(self):
		locateType, locateExpression = self.getTableData['getTableData.row28'.lower()].split('>')
		row8 = getElement(self.driver, locateType, locateExpression)
		return row8.text
	def row38(self):
		locateType, locateExpression = self.getTableData['getTableData.row38'.lower()].split('>')
		row8 = getElement(self.driver, locateType, locateExpression)
		return row8.text

	def row19(self):
		locateType, locateExpression = self.getTableData['getTableData.row19'.lower()].split('>')
		row9 = getElement(self.driver, locateType, locateExpression)
		return row9.text
	def row29(self):
		locateType, locateExpression = self.getTableData['getTableData.row29'.lower()].split('>')
		row9 = getElement(self.driver, locateType, locateExpression)
		return row9.text
	def row39(self):
		locateType, locateExpression = self.getTableData['getTableData.row39'.lower()].split('>')
		row9 = getElement(self.driver, locateType, locateExpression)
		return row9.text

	def row110(self):
		locateType, locateExpression = self.getTableData['getTableData.row110'.lower()].split('>')
		row10 = getElement(self.driver, locateType, locateExpression)
		return row10.text
	def row210(self):
		locateType, locateExpression = self.getTableData['getTableData.row210'.lower()].split('>')
		row10 = getElement(self.driver, locateType, locateExpression)
		return row10.text
	def row310(self):
		locateType, locateExpression = self.getTableData['getTableData.row310'.lower()].split('>')
		row10 = getElement(self.driver, locateType, locateExpression)
		return row10.text

	def row111(self):
		locateType, locateExpression = self.getTableData['getTableData.row111'.lower()].split('>')
		row11= getElement(self.driver, locateType, locateExpression)
		return row11.text
	def row211(self):
		locateType, locateExpression = self.getTableData['getTableData.row211'.lower()].split('>')
		row11= getElement(self.driver, locateType, locateExpression)
		return row11.text
	def row311(self):
		locateType, locateExpression = self.getTableData['getTableData.row311'.lower()].split('>')
		row11= getElement(self.driver, locateType, locateExpression)
		return row11.text

	def row112(self):
		locateType, locateExpression = self.getTableData['getTableData.row112'.lower()].split('>')
		row12 = getElement(self.driver, locateType, locateExpression)
		return row12.text
	def row212(self):
		locateType, locateExpression = self.getTableData['getTableData.row212'.lower()].split('>')
		row12 = getElement(self.driver, locateType, locateExpression)
		return row12.text
	def row312(self):
		locateType, locateExpression = self.getTableData['getTableData.row312'.lower()].split('>')
		row12 = getElement(self.driver, locateType, locateExpression)
		return row12.text

	def row113(self):
		locateType, locateExpression = self.getTableData['getTableData.row113'.lower()].split('>')
		row13 = getElement(self.driver, locateType, locateExpression)
		return row13.text
	def row213(self):
		locateType, locateExpression = self.getTableData['getTableData.row213'.lower()].split('>')
		row13 = getElement(self.driver, locateType, locateExpression)
		return row13.text
	def row313(self):
		locateType, locateExpression = self.getTableData['getTableData.row313'.lower()].split('>')
		row13 = getElement(self.driver, locateType, locateExpression)
		return row13.text

	def row114(self):
		locateType, locateExpression = self.getTableData['getTableData.row114'.lower()].split('>')
		row14 = getElement(self.driver, locateType, locateExpression)
		return row14.text
	def row214(self):
		locateType, locateExpression = self.getTableData['getTableData.row214'.lower()].split('>')
		row14 = getElement(self.driver, locateType, locateExpression)
		return row14.text
	def row314(self):
		locateType, locateExpression = self.getTableData['getTableData.row314'.lower()].split('>')
		row14 = getElement(self.driver, locateType, locateExpression)
		return row14.text

	def row115(self):
		locateType, locateExpression = self.getTableData['getTableData.row115'.lower()].split('>')
		row15 = getElement(self.driver, locateType, locateExpression)
		return row15.text
	def row215(self):
		locateType, locateExpression = self.getTableData['getTableData.row215'.lower()].split('>')
		row15 = getElement(self.driver, locateType, locateExpression)
		return row15.text
	def row315(self):
		locateType, locateExpression = self.getTableData['getTableData.row315'.lower()].split('>')
		row15 = getElement(self.driver, locateType, locateExpression)
		return row15.text

	def row116(self):
		locateType, locateExpression = self.getTableData['getTableData.row116'.lower()].split('>')
		row16 = getElement(self.driver, locateType, locateExpression)
		return row16.text
	def row216(self):
		locateType, locateExpression = self.getTableData['getTableData.row216'.lower()].split('>')
		row16 = getElement(self.driver, locateType, locateExpression)
		return row16.text
	def row316(self):
		locateType, locateExpression = self.getTableData['getTableData.row316'.lower()].split('>')
		row16 = getElement(self.driver, locateType, locateExpression)
		return row16.text