'''
封装添加物业性质独立功能
'''


from PageObject.addPropertyPage import *
from toolKit.log import *
from toolKit.highLightElement import *


def addProperty(driver, propertyNum='', propertyName=''):
	app = AddPropertyPage(driver)
	logger.info(u'测试添加物业性质')
	app.tenancyManagement().click()
	logger.info(u'点击租务管理')
	app.basicSetting().click()
	logger.info(u'点击基础设置')
	app.propertyManagement().click()
	logger.info(u'点击物业性质管理')
	driver.switch_to.frame(app.frameOfPropertyManagement())
	time.sleep(4)
	highLightElement(driver, app.add())
	app.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.frame(app.frameOfAddProperty())
	highLightElement(driver, app.propertyNumBox())
	app.propertyNumBox().click()
	app.propertyNum().send_keys(propertyNum)
	logger.info(u'输入物业性质编码：%s' % propertyNum)
	highLightElement(driver, app.propertyNameBox())
	app.propertyNameBox().click()
	app.propertyName().send_keys(propertyName)
	logger.info(u'输入物业性质编码：%s' % propertyName)
	highLightElement(driver, app.save())
	app.save().click()
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % app.information())
