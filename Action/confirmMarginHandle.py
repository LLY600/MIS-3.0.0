'''
确认保证金处理
'''
from PageObject.confirmMarginHandlePage import *
from PageObject.tableDataPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from prettytable import PrettyTable
from time import sleep


def get_margin_handle_data(driver, contractName):  # 获取保证金处理列表数据
	mhc = MarginHandleConfirmPage(driver)
	logger.info(u'测试保证金处理确认')
	mhc.financialManagement().click()
	logger.info(u'点击财务管理')
	mhc.marginManagement().click()
	logger.info(u'点击保证金管理')
	mhc.marginHandleConfirmMenu().click()
	logger.info(u'点击保证金处理确认')
	driver.switch_to.frame(mhc.frameOfMarginHandleConfirm())
	sleep(4)
	# highLightElement(driver, mhc.contractName())
	mhc.contractName().click()
	logger.info(u'点击合同号文本框')
	# highLightElement(driver, mhc.contractNameInput())
	mhc.contractNameInput().send_keys(contractName)
	sleep(1)
	logger.info(u'输入合同号%s' % contractName)
	highLightElement(driver, mhc.search())
	mhc.search().click()
	logger.info(u'点击列表搜索按钮')
	sleep(1)
	highLightElement(driver, mhc.contactResult())
	mhc.contactResult().click()
	logger.info(u'选择搜索列表合同数据')
	highLightElement(driver, mhc.searchBox())
	mhc.searchBox().click()
	sleep(1)
	logger.info(u'选择文本框搜索按钮')
	sleep(2)
	gtd = GetTableData(driver)
	fileName = listData + 'confirm_margin_handle_data.log'
	table = PrettyTable(['购物中心', '状态', '合同号', '经营商户', '处理时间', '处理金额', '处理类型'])
	table.align['购物中心'] = '1'
	table.padding_width = 1
	table.add_row([gtd.row15(), gtd.row17(), gtd.row18(), gtd.row19(), gtd.row110(), gtd.row111(), gtd.row112()])
	# table.add_row([gtd.row25(), gtd.row27(), gtd.row28(), gtd.row29(), gtd.row210(), gtd.row211(), gtd.row212()])
	# table.add_row([gtd.row35(), gtd.row37(), gtd.row38(), gtd.row39(), gtd.row310(), gtd.row311(), gtd.row312()])
	logger.info(u'正在获取列表数据')
	sleep(1)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'将列表数据写入文件，保存位置:%s' % fileName)

def confirm_margin_handle_data(driver):  # 确认列表数据
	mhc = MarginHandleConfirmPage(driver)
	mhc.select().click()
	logger.info(u'选择保证金处理单号')
	sleep(1)
	mhc.confirm().click()
	logger.info(u'点击文本框确认按钮')
	mhc.infomationConfirm().click()
	logger.info(u'点击提示信息')
	sleep(2)
	logger.info(u'提示信息:%s' % mhc.information())
