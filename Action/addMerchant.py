'''
添加商户功能
'''

from PageObject.addMerchantPage import *
from PageObject.tableDataPage import *
from toolKit.handleKey import *
from toolKit.highLightElement import *
from prettytable import PrettyTable
from time import sleep

def add_merchant_data(driver, merchantNum='', merchantName=''):
	amp = AddMerchantPage(driver)
	amp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	amp.investmentResourcesManagement().click()
	logger.info(u'点击招商资源管理')
	amp.merchantManagement().click()
	logger.info(u'点击商户库管理')
	driver.switch_to.frame(amp.frameOfMerchantManagement())
	sleep(4)
	highLightElement(driver, amp.add())
	amp.add().click()
	logger.info(u'点击添加按钮')
	sleep(1)
	handleAlert(5, 'enter')
	driver.switch_to.default_content()
	driver.switch_to.frame(amp.frameOfAddMerchant())
	sleep(2)
	# 部分系统购物中心、商户编码自动填写，这里需捕获异常
	try:
		highLightElement(driver, amp.mallNameBox())
		amp.mallName().click()
		sleep(0.5)
		amp.mallNameSelect().click()
		highLightElement(driver, amp.merchantNumBox())
		amp.merchantNum().send_keys(merchantNum)
		logger.info(u'输入商户编码：%s' % merchantNum)
	except:
		pass
	highLightElement(driver, amp.merchantNameBox())
	amp.merchantName().send_keys(merchantName)
	logger.info(u'输入商户名称：%s' % merchantName)
	highLightElement(driver, amp. merchantPropertyBox())
	amp.merchantProperty().click()
	amp.merchantPropertyOfValue().click()
	logger.info(u'选择商户性质')
	highLightElement(driver, amp.save())
	amp.save().click()
	logger.info(u'点击添加按钮')
	sleep(1)
	logger.info(u'提示信息：%s' % amp.information())

def get_merchant_data(driver, merchant=''):
	logger.info(u'获取商户列表数据')
	amp = AddMerchantPage(driver)
	sleep(1)
	amp.confirm().click()
	logger.info(u'点击确定按钮')
	driver.switch_to.default_content()
	driver.switch_to.frame(amp.frameOfMerchantManagement())
	sleep(3)
	amp.merchant().send_keys(merchant)
	logger.info(u'输入商户名称：%s' % merchant)
	amp.search().click()
	logger.info(u'点击搜索按钮')
	gtd = GetTableData(driver)
	fileName = listData + u'add_merchant_data.log'
	table = PrettyTable(['商户中文名称', '状态', '版本号', '商户性质'])
	table.align['商户中文名称'] = '1'
	table.padding_width = 1
	sleep(2)
	table.add_row([gtd.row16(), gtd.row18(), gtd.row19(), gtd.row110()])
	logger.info(u'正在获取列表数据')
	sleep(2)
	print(table)
	with open(fileName, 'a') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'保存位置:%s' % fileName)
