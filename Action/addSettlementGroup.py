'''
封装添加结算组别
'''

from PageObject.tableDataPage import *
from PageObject.addSettlementGroupPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from prettytable import PrettyTable
from time import sleep


def add_settlement_group_data(driver, settlementGroupNum='', settlementGroupName=''):
	asgp = AddSettlementGroupPage(driver)
	logger.info(u'测试添加结算组别')
	asgp.tenancyManagement().click()
	logger.info(u'点击财务管理')
	asgp.basicSetting().click()
	logger.info(u'点击基础设置')
	asgp.settlementGroupManagement().click()
	logger.info(u'点击结算组别管理')
	driver.switch_to.frame(asgp.frameOfSettlementGroupManagement())
	sleep(4)
	highLightElement(driver, asgp.add())
	asgp.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.frame(asgp.frameOfAddSettlementGroup())
	highLightElement(driver, asgp.settlementGroupNumBox())
	asgp.settlementGroupNum().send_keys(settlementGroupNum)
	logger.info(u'输入结算组别编码：%s' % settlementGroupNum)
	highLightElement(driver, asgp.settlementGroupNameBox())
	asgp.settlementGroupName().send_keys(settlementGroupName)
	logger.info(u'输入结算组别名称：%s' % settlementGroupName)
	highLightElement(driver, asgp.save())
	asgp.save().click()
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % asgp.information())

def get_settlement_group_data(driver, settlementGroupNum=''):
	asgp = AddSettlementGroupPage(driver)
	highLightElement(driver, asgp.confirm())
	asgp.confirm().click()
	driver.switch_to.default_content()
	driver.switch_to.frame(asgp.frameOfSettlementGroupManagement())
	sleep(2)
	asgp.settlementGroupNum().send_keys(settlementGroupNum)
	asgp.search().click()
	sleep(2)
	gtd = GetTableData(driver)
	fileName = listData + 'add_settlement_group_data.log'
	table = PrettyTable(['结算组别编码', '结算组别名称'])
	table.align['结算组别编码'] = '1'
	table.padding_width = 1
	table.add_row([gtd.row14(), gtd.row15()])
	logger.info(u'正在获取列表数据')
	sleep(2)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'保存位置:%s' % fileName)
