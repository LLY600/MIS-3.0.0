'''
封装账单调整确认独立功能
'''

from selenium import webdriver
from PageObject.confirmBillAdjustPage import *
from PageObject.tableDataPage import *
from toolKit.log import *
from toolKit.highLightElement import *


def billAdjustConfirmList(driver, contractName=''):
	bacp = BillAdjustConfirmPage(driver)
	logger.info(u'测试账单调整确认')
	driver.implicitly_wait(5)
	bacp.financialManagement().click()
	logger.info(u'点击财务管理')
	bacp.billAdjust().click()
	logger.info(u'点击账单调整模块')
	bacp.billAdjustConfirm().click()
	logger.info(u'点击账单调整确认')
	driver.switch_to.frame(bacp.frameOfBillAdjustConfirm())
	time.sleep(3)
	highLightElement(driver, bacp.contract())
	bacp.contract().click()
	logger.info(u'点击合同号文本框')
	highLightElement(driver, bacp.contractInput())
	bacp.contractInput().send_keys(contractName)
	logger.info(u'输入合同号：%s' % contractName)
	highLightElement(driver, bacp.contractSearch())
	bacp.contractSearch().click()
	logger.info(u'点击合同号搜索按钮')
	highLightElement(driver, bacp.contractSearchResult())
	bacp.contractSearchResult().click()
	logger.info(u'选择合同号搜索结果')
	highLightElement(driver, bacp.search())
	bacp.search().click()
	logger.info(u'选择搜索按钮')
	time.sleep(1)
	gtd = GetTableData(driver)
	fileName = listData + 'billAdjustConfirmList.log'
	table = PrettyTable(['购物中心', '状态', '经营商户', '经营店铺', '合同号', '调整账单号', '本次调整金额'])
	table.align['购物中心'] = '1'
	table.padding_width = 1
	table.add_row([gtd.row14(), gtd.row16(), gtd.row17(), gtd.row18(), gtd.row19(), gtd.row110(), gtd.row111()])
	logger.info(u'正在获取列表数据')
	time.sleep(1)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
	logger.info(u'将列表数据写入文件，保存位置:%s' % fileName)

def billAdjustConfirmSelect(driver):
	bacp = BillAdjustConfirmPage(driver)
	highLightElement(driver, bacp.select())
	bacp.select().click()
	logger.info(u'选择账单调整记录')
	highLightElement(driver, bacp.confirmButton())
	bacp.confirmButton().click()
	logger.info(u'点击确认按钮')
	highLightElement(driver, bacp.confirm())
	bacp.confirm().click()
	logger.info(u'点击“是”，账单调整确认')
	logger.info(u'提示信息：%s' % (bacp.information()))