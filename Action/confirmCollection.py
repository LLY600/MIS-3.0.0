'''
封装收款确认独立功能
'''

from selenium import webdriver
from PageObject.addCollectionConfirmPage import *
from PageObject.listTableDataPage import *
from toolKit.log import *
from toolKit.highLightElement import *


def collectionConfirmList(driver, contractName=''):
	accp = AddCollectionConfirmPage(driver)
	logger.info(u'测试收款确认')
	driver.implicitly_wait(5)
	accp.financialManagement().click()
	logger.info(u'点击财务管理')
	accp.collectionManagement().click()
	logger.info(u'点击收款管理')
	accp.collectionConfirm().click()
	logger.info(u'点击收款确认')
	driver.switch_to.frame(accp.frameOfCollectionConfirm())
	time.sleep(4)
	highLightElement(driver, accp.contract())
	accp.contract().click()
	logger.info(u'点击合同号文本框')
	highLightElement(driver, accp.contractInput())
	accp.contractInput().send_keys(contractName)
	logger.info(u'输入合同号：%s' % contractName)
	highLightElement(driver, accp.contractSearch())
	accp.contractSearch().click()
	logger.info(u'点击合同搜索按钮')
	highLightElement(driver, accp.contractSearchResult())
	accp.contractSearchResult().click()
	logger.info(u'选择合同搜索结果')
	highLightElement(driver, accp.collectionType())
	accp.collectionType().click()
	logger.info(u'点击收款类别文本框')
	highLightElement(driver, accp.collectionTypeSelect())
	accp.collectionTypeSelect().click()
	logger.info(u'选择收款类别')
	highLightElement(driver, accp.search())
	accp.search().click()
	logger.info(u'点击搜索按钮')
	time.sleep(2)
	gtd = GetTableData(driver)
	fileName = listData + 'collectionConfirmList.log'
	table = PrettyTable(
		['购物中心', '类别', '状态', '经营商户', '经营店铺', '合同号', '账单号', '收款金额', '未收款金额', '收款时间'])
	table.align['购物中心'] = '1'
	table.padding_width = 1
	table.add_row([gtd.row14(), gtd.row16(), gtd.row17(), gtd.row18(), gtd.row19(), gtd.row110(), gtd.row111(), gtd.row112(), gtd.row113(), gtd.row114()])
	logger.info(u'正在获取列表数据')
	time.sleep(2)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
	logger.info(u'保存位置:%s' % fileName)

def collectionConfirmSelect(driver):
	accp = AddCollectionConfirmPage(driver)
	highLightElement(driver, accp.select())
	accp.select().click()
	logger.info(u'选择收款单号')
	highLightElement(driver, accp.confirm())
	accp.confirm().click()
	logger.info(u'点击确认按钮')
	highLightElement(driver, accp.confirmCollection())
	accp.confirmCollection().click()
	logger.info(u'确认收款单')
	logger.info(u'提示信息：%s' % (accp.information()))
