'''
封装确认商户功能
'''

from PageObject.confirmMerchantPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from PageObject.tableDataPage import *
from prettytable import PrettyTable
from time import sleep

def get_merchant_data(driver, brand=''):
	cmp = ConfirmMerchantPage(driver)
	logger.info(u'测试确认商户信息')
	cmp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	cmp.investmentResourcesManagement().click()
	logger.info(u'点击招商资源管理')
	cmp.merchantConfirm().click()
	logger.info(u'点击商户信息确认')
	driver.switch_to.frame(cmp.frameOfMerchantConfirm())
	sleep(4)
	highLightElement(driver, cmp.merchantBox())
	cmp.merchant().send_keys(brand)
	logger.info(u'输入商户名称：%s' % brand)
	highLightElement(driver, cmp.search())
	cmp.search().click()
	logger.info(u'点击搜索按钮')
	sleep(2)
	gtd = GetTableData(driver)
	fileName = listData + 'confirm_merchant_data.log'
	table = PrettyTable(['商户中文名称', '状态', '版本号', '商户性质'])
	table.align['商户中文名称'] = '1'
	table.padding_width = 1
	table.add_row([gtd.row16(), gtd.row18(), gtd.row19(), gtd.row110()])
	logger.info(u'正在获取列表数据')
	sleep(2)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'保存位置:%s' % fileName)


def confirm_merchant_data(driver):
	cmp = ConfirmMerchantPage(driver)
	highLightElement(driver, cmp.select())
	cmp.select().click()
	logger.info(u'选择商户')
	highLightElement(driver, cmp.confirmButton())
	cmp.confirmButton().click()
	logger.info(u'点击确认按钮')
	time.sleep(1)
	highLightElement(driver, cmp.confirm())
	cmp.confirm().click()
	logger.info(u'确认商户')
	logger.info(u'提示信息：%s' % (cmp.information()))
