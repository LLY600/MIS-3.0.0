'''
账单生成功能
'''

from PageObject.addBillGenerationPage import *
from PageObject.tableDataPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from prettytable import PrettyTable
from time import sleep


def add_bill_generation(driver, settlementDate='', contract=''):
	bgp = BillGenerationPage(driver)
	logger.info(u'测试账单生成')
	bgp.financialManagement().click()
	logger.info(u'点击财务管理')
	bgp.billManagement().click()
	logger.info(u'点击账单管理')
	bgp.billGeneration().click()
	logger.info(u'点击账单处理（账单生成）')
	driver.switch_to.frame(bgp.frameOfBillGeneration())
	sleep(4)
	# highLightElement(driver, bgp.settlementDate())
	bgp.settlementDate().send_keys(settlementDate)
	logger.info(u'输入结算日期：%s' % settlementDate)
	# highLightElement(driver, bgp.contractName())
	bgp.contractName().click()
	logger.info(u'点击合同号文本框')
	# highLightElement(driver, bgp.contractNameInput())
	bgp.contractNameInput().send_keys(contract)
	logger.info(u'输入合同号：%s' % contract)
	highLightElement(driver, bgp.contractNameSearch())
	bgp.contractNameSearch().click()
	logger.info(u'点击搜索按钮')
	highLightElement(driver, bgp.contractNameSearchResult())
	bgp.contractNameSearchResult().click()
	logger.info(u'选择搜索结果')
	highLightElement(driver, bgp.button())
	bgp.button().click()
	logger.info(u'点击生成账单')
	logger.info(u'提示信息：%s' % (bgp.information()))
	highLightElement(driver, bgp.confirm())

def get_bill_data(driver):
	sleep(1.5)
	bgp = BillGenerationPage(driver)
	bgp.confirm().click()
	driver.switch_to.default_content()
	driver.switch_to.frame(bgp.frameOfBillGeneration())
	gtd = GetTableData(driver)
	fileName = listData + 'add_bill_generation_data.log'
	table = PrettyTable(
		['购物中心', '账单号', '状态', '经营商户', '经营店铺', '结算组别', '合同号', '账期', '结算开始时间', '结算结束时间', '滞纳金起算时间', '费用金额'])
	table.align['购物中心'] = '1'
	table.padding_width = 1
	# 因其他账单类似，这里仅获取第一条记录
	table.add_row([gtd.row14(), gtd.row15(), gtd.row17(), gtd.row18(), gtd.row19(), gtd.row110(), gtd.row111(), gtd.row112(), gtd.row113(), gtd.row114(), gtd.row115(), gtd.row116()])
	# table.add_row([gtd.row24(), gtd.row25(), gtd.row27(), gtd.row28(), gtd.row29(), gtd.row210(), gtd.row211(), gtd.row212(), gtd.row213(), gtd.row214(), gtd.row215(), gtd.row216()])
	logger.info(u'正在获取列表数据')
	sleep(1)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'将列表数据写入文件，保存位置:%s' % fileName)