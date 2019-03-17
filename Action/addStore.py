'''
添加店铺信息功能
'''

from time import sleep
from PageObject.addStorePage import *
from PageObject.tableDataPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from prettytable import PrettyTable


def add_store_data(driver, storeNum='', storeName='', merchantName='', brandName='', mainBrandName=''):
	asp = AddStorePage(driver)
	logger.info(u'测试添加店铺信息')
	asp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	asp.investmentResourcesManagement().click()
	logger.info(u'点击招商资源管理')
	asp.storeManagement().click()
	logger.info(u'点击店铺管理')
	driver.switch_to.frame(asp.frameOfStoreManagement())
	sleep(4)
	highLightElement(driver, asp.add())
	asp.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.frame(asp.frameOfAddStore())
	sleep(4)
	highLightElement(driver, asp.storeNumBox())
	asp.storeNum().send_keys(storeNum)
	logger.info(u'输入店铺编码：%s' % storeNum)
	highLightElement(driver, asp.storeNameBox())
	asp.storeName().send_keys(storeName)
	logger.info(u'输入店铺名称：%s' % storeName)
	highLightElement(driver, asp.salesTypeBox())
	asp.salesType().click()
	asp.salesTypeSelect().click()
	logger.info(u'选择销售数据采集方式')
	#  有的系统购物中心字段系统默认填写，因此这里需要捕获异常
	try:
		highLightElement(driver, asp.mallNameBox())
		asp.mallName().click()
		sleep(1)
		asp.mallNameSelect().click()
		logger.info(u'选择购物中心')
	except:
		pass
	highLightElement(driver, asp.merchantBox())
	asp.merchant().click()
	highLightElement(driver, asp.merchantInputBox())
	asp.merchantInput().send_keys(merchantName)
	logger.info(u'输入商户名称：%s' % merchantName)
	sleep(0.5)
	highLightElement(driver, asp.merchantSearch())
	asp.merchantSearch().click()
	logger.info(u'点击商户搜索按钮')
	sleep(1)
	highLightElement(driver, asp.merchantSelect())
	asp.merchantSelect().click()
	logger.info(u'选择商户搜索结果')
	highLightElement(driver, asp.brandBox())
	asp.brand().click()
	highLightElement(driver, asp.brandInputBox())
	asp.brandInput().send_keys(brandName)
	logger.info(u'输入品牌名称：%s' % brandName)
	sleep(0.5)
	highLightElement(driver, asp.brandSearch())
	asp.brandSearch().click()
	logger.info(u'点击品牌搜索按钮')
	sleep(1)
	highLightElement(driver, asp.brandSelect())
	asp.brandSelect().click()
	logger.info(u'选择品牌搜索结果')
	highLightElement(driver, asp.mainBrandBox())
	asp.mainBrand().click()
	highLightElement(driver, asp.mainBrandInputBox())
	asp.mainBrandInput().send_keys(mainBrandName)
	logger.info(u'输入主品牌名称：%s' % mainBrandName)
	sleep(0.5)
	highLightElement(driver, asp.mainBrandSearch())
	asp.mainBrandSearch().click()
	logger.info(u'点击主品牌搜索按钮')
	sleep(1)
	highLightElement(driver, asp.mainBrandSelect())
	asp.mainBrandSelect().click()
	logger.info(u'选择主品牌搜索结果')
	highLightElement(driver, asp.save())
	asp.save().click()
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % asp.information())

def get_store_data(driver, store=''):
	asp = AddStorePage(driver)
	highLightElement(driver, asp.confirm())
	asp.confirm().click()
	driver.switch_to.default_content()
	driver.switch_to.frame(asp.frameOfStoreManagement())
	sleep(2)
	highLightElement(driver, asp.storeNameListBox())
	asp.storeNameList().send_keys(store)
	highLightElement(driver, asp.search())
	asp.search().click()
	sleep(2)
	gtd = GetTableData(driver)
	fileName = listData + 'add_store_data.log'
	table = PrettyTable(['店铺名称', '店铺编号', '经营品牌', '主品牌', '店铺状态', '商户名称'])
	table.align['店铺名称'] = '1'
	table.padding_width = 1
	table.add_row([gtd.row16(), gtd.row17(), gtd.row18(), gtd.row19(), gtd.row110(), gtd.row111()])
	logger.info(u'正在获取列表数据')
	sleep(2)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'保存位置:%s' % fileName)

