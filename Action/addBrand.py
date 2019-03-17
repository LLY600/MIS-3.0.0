'''
添加品牌功能
'''

from time import sleep
from PageObject.addBrandPage import *
from PageObject.tableDataPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from prettytable import PrettyTable


def add_brand(driver, brandNum='', brandName='', company='', leader='', address='', phone=''):
	abp = AddBrandPage(driver)
	logger.info(u'测试添加品牌信息')
	abp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	abp.investmentResourcesManagement().click()
	logger.info(u'点击招商资源管理')
	abp.brandManagement().click()
	logger.info(u'点击品牌管理')
	driver.switch_to.frame(abp.frameOfBrandManagement())
	sleep(4)
	highLightElement(driver, abp.add())
	abp.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.frame(abp.frameOfAddBrand())
	sleep(3)
	# 部分系统品牌编码系统自动填写，这里需捕获异常
	try:
		highLightElement(driver, abp.brandNumBox())
		abp.brandNum().send_keys(brandNum)
		logger.info(u'输入品牌编码：%s' % brandNum)
	except:
		pass
	highLightElement(driver, abp.brandNameBox())
	abp.brandNameInput().send_keys(brandName)
	logger.info(u'输入品牌名称：%s' % brandName)
	highLightElement(driver, abp.merchandisingBox())
	abp.merchandising().click()
	sleep(0.5)
	abp.merchandisingSelect().click()
	logger.info(u'选择业态')
	try:
		highLightElement(driver, abp.companyBox())
		abp.company().send_keys(company)
		logger.info(u'输入所属公司：%s' % company)
		highLightElement(driver, abp.leaderBox())
		abp.leader().send_keys(leader)
		logger.info(u'输入负责人：%s' % leader)
		highLightElement(driver, abp.addressBox())
		abp.address().send_keys(address)
		logger.info(u'输入联系地址：%s' % address)
		highLightElement(driver, abp.phoneBox())
		abp.phone().send_keys(phone)
		logger.info(u'输入联系电话：%s' % phone)
	except:
		pass
	highLightElement(driver, abp.save())
	abp.save().click()
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % abp.information())

def add_brand_data(driver, brand=''):
	logger.info(u'获取品牌列表数据')
	abp = AddBrandPage(driver)
	abp.confirm().click()
	logger.info(u'点击确定按钮')
	driver.switch_to.default_content()
	driver.switch_to.frame(abp.frameOfBrandManagement())
	sleep(3)
	abp.brandNameInput().send_keys(brand)
	logger.info(u'输入品牌名称：%s' % brand)
	abp.search().click()
	logger.info(u'点击搜索按钮')
	gtd = GetTableData(driver)
	fileName = listData + u'add_brand_data.log'
	table = PrettyTable(
		['品牌名称', '状态', '规划业态'])
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
