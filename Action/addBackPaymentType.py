'''
封装后台收款方式
'''

from time import sleep
from PageObject.addBackPaymentTypePage import *
from toolKit.log import *
from toolKit.highLightElement import *


def addBackPaymentType(driver, paymentTypeNum='', paymentType=''):
	abptp = AddBackPaymentTypePage(driver)
	logger.info(u'测试添加后台收款方式')
	abptp.financialManagement().click()
	logger.info(u'点击财务管理')
	abptp.basicSetting().click()
	logger.info(u'点击基础设置')
	abptp.backPaymentType().click()
	logger.info(u'点击后台收款方式维护')
	driver.switch_to.frame(abptp.frameOfBackPaymentType())
	sleep(4)
	highLightElement(driver, abptp.add())
	abptp.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.frame(abptp.frameOfAddBackPaymentType())
	sleep(2)
	highLightElement(driver, abptp.paymentTypeNumBox())
	abptp.paymentTypeNum().send_keys(paymentTypeNum)
	logger.info(u'输入收款方式编码：%s' % paymentTypeNum)
	highLightElement(driver, abptp.paymentTypeBox())
	abptp.paymentType().send_keys(paymentType)
	logger.info(u'输入收款方式名称：%s' % paymentType)
	highLightElement(driver, abptp.save())
	abptp.save().click()
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % abptp.information())
