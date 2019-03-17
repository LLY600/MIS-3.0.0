'''
封装确认品牌独立功能
'''

from time import sleep
from PageObject.confirmBrandPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from PageObject.tableDataPage import *
from prettytable import PrettyTable

def get_brand_data(driver, brand=''):
	cbp = ConfirmBrandPage(driver)
	logger.info(u'测试确认品牌信息')
	cbp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	cbp.investmentResourcesManagement().click()
	logger.info(u'点击招商资源管理')
	cbp.brandConfirm().click()
	logger.info(u'点击品牌信息确认')
	driver.switch_to.frame(cbp.frameOfBrandConfirm())
	sleep(4)
	highLightElement(driver, cbp.brandBox())
	cbp.brand().send_keys(brand)
	logger.info(u'输入品牌名称：%s' % brand)
	highLightElement(driver, cbp.search())
	cbp.search().click()
	logger.info(u'点击搜索按钮')
	sleep(2)
	gtd = GetTableData(driver)
	fileName = listData + u'confirm_brand_data.log'
	table = PrettyTable(['品牌名称', '状态', '规划业态'])
	table.align['品牌名称'] = '1'
	table.padding_width = 1
	sleep(2)
	table.add_row([gtd.row15(), gtd.row16(), gtd.row17()])
	logger.info(u'正在获取列表数据')
	sleep(2)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'保存位置:%s' % fileName)


def confirm_brand(driver):
	cbp = ConfirmBrandPage(driver)
	highLightElement(driver, cbp.select())
	cbp.select().click()
	logger.info(u'选择品牌')
	highLightElement(driver, cbp.confirmButton())
	cbp.confirmButton().click()
	logger.info(u'点击确认按钮')
	time.sleep(1)
	highLightElement(driver, cbp.confirm())
	cbp.confirm().click()
	logger.info(u'确认品牌')
	logger.info(u'提示信息：%s' % (cbp.information()))
