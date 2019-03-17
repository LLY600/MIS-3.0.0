'''
添加集团功能
'''

from PageObject.addGroupPage import *
from toolKit.log import *
# from toolKit.highLightElement import *
from time import sleep

def add_group_data(driver, groupNum='', groupName=''):
	agp = AddGroupPage(driver)
	logger.info(u'测试添加集团信息')
	agp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	agp.propertyManagement().click()
	logger.info(u'点击资产管理')
	agp.groupManagement().click()
	logger.info(u'点击集团管理')
	driver.switch_to.frame(agp.frameOfGroupManagement())
	sleep(4)
	agp.add().click()
	logger.info(u'点击添加按钮')
	sleep(2)
	driver.switch_to.frame(agp.frameOfAddGroupManagement())
	agp.groupNum().send_keys(groupNum)
	logger.info(u'输入集团编号：%s' % groupNum)
	agp.groupName().send_keys(groupName)
	logger.info(u'输入集团名称：%s' % groupName)
	agp.add().click()
	logger.info(u'点击添加按钮')
	sleep(0.5)
	logger.info(u'提示信息：%s' % (agp.information()))
