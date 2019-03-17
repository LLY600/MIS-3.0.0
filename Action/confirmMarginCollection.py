
from PageObject.confirmMarginCollectionPage import *
from PageObject.tableDataPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from prettytable import PrettyTable
from time import sleep


def get_margin_collection_data(driver, contract):  # 获取保证金收取列表数据
	mcc = MarginCollectionConfirmPage(driver)
	logger.info(u'测试保证金收取确认')
	mcc.financialManagement().click()
	logger.info(u'点击财务管理')
	mcc.marginManagement().click()
	logger.info(u'点击保证金管理')
	mcc.marginCollectionConfirm().click()
	logger.info(u'点击保证金收取确认')
	driver.switch_to.frame(mcc.frameOfCollectionConfirm())
	sleep(4)
	highLightElement(driver, mcc.contractName())
	mcc.contractName().click()
	logger.info(u'点击合同号文本框')
	highLightElement(driver, mcc.contractNameInput())
	mcc.contractNameInput().send_keys(contract)
	logger.info(u'输入合同号%s' % contract)
	highLightElement(driver, mcc.search())
	mcc.search().click()
	logger.info(u'点击列表搜索按钮')
	sleep(1)
	highLightElement(driver, mcc.contactResult())
	mcc.contactResult().click()
	logger.info(u'选择搜索列表合同数据')
	highLightElement(driver, mcc.searchBox())
	mcc.searchBox().click()
	sleep(1)
	logger.info(u'选择文本框搜索按钮')
	sleep(2)
	gtd = GetTableData(driver)
	fileName = listData + 'confirm_margin_collection_data.log'
	table = PrettyTable(['购物中心', '状态', '类别', '合同号', '经营商户', '经营店铺', '收款金额', '收款时间'])
	table.align['购物中心'] = '1'
	table.padding_width = 1
	table.add_row([gtd.row15(), gtd.row16(), gtd.row17(), gtd.row18(), gtd.row19(), gtd.row110(), gtd.row111(), gtd.row112()])
	logger.info(u'正在获取列表数据')
	sleep(2)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'将列表数据写入文件，保存位置:%s' % fileName)


def confirm_margin_collection(driver):  # 确认列表记录
	mcc = MarginCollectionConfirmPage(driver)
	highLightElement(driver, mcc.select())
	mcc.select().click()
	logger.info(u'选择保证金收款单号')
	highLightElement(driver, mcc.confirm())
	mcc.confirm().click()
	logger.info(u'点击文本框确认按钮')
	highLightElement(driver, mcc.infomationConfirm())
	mcc.infomationConfirm().click()
	logger.info(u'点击提示信息')
	sleep(2)
	logger.info(u'提示信息:%s' % mcc.information())