'''
封装账单确认独立功能
'''

from prettytable import PrettyTable
from PageObject.confirmBillPage import *
from PageObject.tableDataPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from time import sleep

def get_bill_data(driver, contractName=''):  # 获取账单列表数据
	bcp = BillConfirmPage(driver)
	logger.info(u'测试账单确认')
	bcp.financialManagement().click()
	logger.info(u'点击财务管理')
	bcp.billManagement().click()
	logger.info(u'点击账单管理')
	bcp.billConfirm().click()
	logger.info(u'点击账单确认')
	driver.switch_to.frame(bcp.frameOfBillConfirm())
	sleep(4)
	# highLightElement(driver, bcp.contractNameInput())
	bcp.contractNameInput().send_keys(contractName)
	logger.info(u'输入合同号：%s' % contractName)
	highLightElement(driver, bcp.search())
	bcp.search().click()
	logger.info(u'点击搜索按钮')
	sleep(2)
	gtd = GetTableData(driver)
	fileName = listData + 'confirm_bill_data.log'
	table = PrettyTable(
		['购物中心', '账单号', '状态', '经营店铺', '经营商户', '结算组别', '合同号', '账期', '结算开始时间', '结算结束时间', '滞纳金起算时间', '费用金额'])
	table.align['购物中心'] = '1'
	table.padding_width = 1
	table.add_row(
		[gtd.row14(), gtd.row15(), gtd.row17(), gtd.row18(), gtd.row19(), gtd.row110(), gtd.row111(), gtd.row112(),
		 gtd.row113(), gtd.row114(), gtd.row115(), gtd.row116()])
	# table.add_row(
	# 	[gtd.row24(), gtd.row25(), gtd.row27(), gtd.row28(), gtd.row29(), gtd.row210(), gtd.row211(), gtd.row212(),
	# 	 gtd.row213(), gtd.row214(), gtd.row215(), gtd.row216()])
	logger.info(u'正在获取列表数据')
	sleep(2)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'保存位置:%s' % fileName)

def confirm_bill_data(driver):  # 确认账单数据
	bcp = BillConfirmPage(driver)
	highLightElement(driver, bcp.select())
	bcp.select().click()
	logger.info(u'选择账单号')
	highLightElement(driver, bcp.confirmButton())
	bcp.confirmButton().click()
	logger.info(u'点击确认按钮')
	highLightElement(driver, bcp.Confirm())
	bcp.Confirm().click()
	logger.info(u'确认账单')
	logger.info(u'提示信息：%s' % (bcp.information()))
