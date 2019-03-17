'''
添加区域功能
'''

from PageObject.addDistrictPage import *
from toolKit.log import *
# from toolKit.highLightElement import *
from time import sleep

def add_district_data(driver, districtNum='', districtName='', districtEName=''):
	adp = AddDistrictPage(driver)
	logger.info(u'测试添加集团信息')
	adp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	adp.propertyManagement().click()
	logger.info(u'点击资产管理')
	adp.districtManagement().click()
	logger.info(u'点击区域管理')
	driver.switch_to.frame(adp.frameOfDistrictManagement())
	sleep(4)
	adp.add().click()
	logger.info(u'点击添加按钮')
	sleep(2)
	driver.switch_to.frame(adp.frameOfAddDistrictManagement())
	adp.districtNum().send_keys(districtNum)
	logger.info(u'输入区域编号：%s' % districtNum)
	adp.districtName().send_keys(districtName)
	logger.info(u'输入区域中文名称：%s' % districtName)
	adp.districtEName().send_keys(districtEName)
	logger.info(u'输入区域英文名称：%s' % districtEName)
	adp.add().click()
	logger.info(u'点击添加按钮')
	sleep(0.5)
	logger.info(u'提示信息：%s' % (adp.information()))
