'''
封装添加账单调整类型
'''

from time import sleep
from PageObject.addBillAdjustTypePage import *
from toolKit.log import *
from toolKit.highLightElement import *


def addBillAdjustType(driver, billAdjustNum='', billAdjustName=''):
	abatp = AddBillAdjustTypePage(driver)
	logger.info(u'测试添加账单调整类型')
	abatp.financialManagement().click()
	logger.info(u'点击财务管理')
	abatp.billAdjust().click()
	logger.info(u'点击账单调整维护')
	abatp.billAdjustType().click()
	logger.info(u'点击账单调整类型维护')
	driver.switch_to.frame(abatp.frameOfBillAdjustType())
	sleep(4)
	highLightElement(driver, abatp.add())
	abatp.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.frame(abatp.frameOfAddBillAdjust())
	sleep(2)
	highLightElement(driver, abatp.billAdjustNumBox())
	abatp.billAdjustNum().send_keys(billAdjustNum)
	logger.info(u'输入编号：%s' % billAdjustNum)
	highLightElement(driver, abatp.billAdjustNameBox())
	abatp.billAdjustName().send_keys(billAdjustName)
	logger.info(u'输入名称：%s' % billAdjustName)
	highLightElement(driver, abatp.save())
	abatp.save().click()
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % abatp.information())
