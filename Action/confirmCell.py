'''
确认单元功能
'''

from time import sleep
from PageObject.confirmCellPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from PageObject.tableDataPage import *
from prettytable import PrettyTable

def get_cell_data(driver, cellNum=''):
	ccp = ConfirmCellPage(driver)
	logger.info(u'测试确认单元信息')
	ccp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	ccp.propertyManagement().click()
	logger.info(u'点击资产管理')
	ccp.cellConfirm().click()
	logger.info(u'点击单元确认')
	driver.switch_to.frame(ccp.frameOfCellConfirm())
	sleep(4)
	highLightElement(driver, ccp.cellNumBox())
	ccp.cellNum().send_keys(cellNum)
	logger.info(u'输入单元号：%s' % cellNum)
	ccp.search().click()
	logger.info(u'点击搜索按钮')
	sleep(2)
	gtd = GetTableData(driver)
	fileName = listData + u'confirm_cell_data.log'
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


def confirm_cell(driver):
	ccp = ConfirmCellPage(driver)
	sleep(1)
	highLightElement(driver, ccp.select())
	ccp.select().click()
	logger.info(u'选择单元号')
	highLightElement(driver, ccp.confirmButton())
	ccp.confirmButton().click()
	logger.info(u'点击确认按钮')
	sleep(1)
	highLightElement(driver, ccp.confirm())
	ccp.confirm().click()
	logger.info(u'确认单元')
	logger.info(u'提示信息：%s' % (ccp.information()))
