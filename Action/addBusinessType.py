'''
封装添加业态独立功能
'''

from PageObject.addBusinessTypePage import *
from toolKit.log import *
from toolKit.highLightElement import *


def addBusinessType(driver, businessTypeNum='', businessTypeName=''):
	abtp = AddBusinessTypePage(driver)
	logger.info(u'测试添加业态')
	abtp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	abtp.basicSetting().click()
	logger.info(u'点击基础设置')
	abtp.businessTypeManagement().click()
	logger.info(u'点击业态管理')
	driver.switch_to.frame(abtp.frameOfBusinessTypeManagement())
	time.sleep(4)
	highLightElement(driver, abtp.add())
	abtp.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.frame(abtp.frameOfAddBusinessType())
	highLightElement(driver, abtp.businessTypeNumBox())
	abtp.businessTypeNumBox().click()
	abtp.businessTypeNum().send_keys(businessTypeNum)
	logger.info(u'输入物业性质编码：%s' % businessTypeNum)
	highLightElement(driver, abtp.businessTypeNameBox())
	abtp.businessTypeNameBox().click()
	abtp.businessTypeName().send_keys(businessTypeName)
	logger.info(u'输入物业性质编码：%s' % businessTypeName)
	highLightElement(driver, abtp.save())
	abtp.save().click()
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % abtp.information())
