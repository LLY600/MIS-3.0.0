'''
封装添加单元独立功能
'''

from PageObject.addCellPage import *
from PageObject.tableDataPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from prettytable import PrettyTable
from time import sleep

def add_cell(driver, cellNum='', buildArea='', area='', cellDescription=''):
	acp = AddCellPage(driver)
	logger.info(u'测试添加单元信息')
	acp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	acp.propertyManagement().click()
	logger.info(u'点击资产管理')
	acp.cellManagement().click()
	logger.info(u'点击单元管理')
	driver.switch_to.frame(acp.frameOfCellManagement())
	sleep(4)
	highLightElement(driver, acp.add())
	acp.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.frame(acp.frameOfAddCell())
	highLightElement(driver, acp.cellNumBox())
	acp.cellNumInput().send_keys(cellNum)
	logger.info(u'输入单元号：%s' % cellNum)
	# 有的MIS系统，购物中心数据默认填写，这里需捕获异常
	try:
		highLightElement(driver, acp.mallBox())
		acp.mall().click()
		sleep(1)
		acp.mallSelect().click()
		logger.info(u'选择购物中心')
	except:
		pass
	highLightElement(driver, acp.merchandisingBox())
	acp.merchandising().click()
	sleep(0.5)
	acp.merchandisingSelect().click()
	logger.info(u'选择规划业态')
	highLightElement(driver, acp.buildingBox())
	acp.building().click()
	sleep(1)
	acp.buildingSelect().click()
	logger.info(u'选择楼宇')
	highLightElement(driver, acp.buildAreaBox())
	acp.buildAreaInput().send_keys(buildArea)
	logger.info(u'输入建筑面积：%s' % buildArea)
	highLightElement(driver, acp.areaBox())
	acp.areaInput().send_keys(area)
	logger.info(u'输入套内面积：%s' % area)
	# 可选参数需要捕获异常
	try:
		highLightElement(driver, acp.cellDescriptionBox())
		acp.cellDescriptionInput().send_keys(cellDescription)
		logger.info(u'输入单元描述：%s' % cellDescription)
	except:
		pass
	highLightElement(driver, acp.save())
	acp.save().click()
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % acp.information())

def add_cell_data(driver, cellNum=''):
	acp = AddCellPage(driver)
	highLightElement(driver, acp.confirm())
	acp.confirm().click()
	logger.info(u'点击确认按钮')
	driver.switch_to.default_content()
	driver.switch_to.frame(acp.frameOfCellManagement())
	sleep(2)
	acp.cellNumInput().send_keys(cellNum)
	logger.info(u'输入单元号：%s' % cellNum)
	acp.search().click()
	sleep(1)
	gtd = GetTableData(driver)
	fileName = listData + u'add_cell_data.log'
	table = PrettyTable(['单元号', '状态', '类别', '楼宇', '规划业态', '建筑面积', '套内面积'])
	table.align['单元号'] = '1'
	table.padding_width = 1
	sleep(2)
	table.add_row([gtd.row15(), gtd.row16(), gtd.row17(), gtd.row18(), gtd.row19(), gtd.row110(), gtd.row111()])
	logger.info(u'正在获取列表数据')
	sleep(2)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'保存位置:%s' % fileName)
