'''
封装添加货品组别独立功能
'''


from PageObject.addCommodityGroupPage import *
from toolKit.log import *
from toolKit.highLightElement import *



def addCommodityGroup(driver, commodityGroupNum='', commodityGroupName=''):
	acgp = AddCommodityGroupPage(driver)
	logger.info(u'测试添加店铺信息')
	acgp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	acgp.investmentResourcesManagement().click()
	logger.info(u'点击招商资源管理')
	acgp.commodityGroupManagement().click()
	logger.info(u'点击货品组别管理')
	driver.switch_to.frame(acgp.frameOfCommodityGroupManagement())
	time.sleep(4)
	highLightElement(driver, acgp.add())
	acgp.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.frame(acgp.frameOfAddCommodityGroup())
	time.sleep(2)
	highLightElement(driver, acgp.commodityGroupNumBox())
	acgp.commodityGroupNum().send_keys(commodityGroupNum)
	logger.info(u'输入货品组别编码：%s' % commodityGroupNum)
	highLightElement(driver, acgp.commodityGroupNameBox())
	acgp.commodityGroupName().send_keys(commodityGroupName)
	logger.info(u'输入货品组别名称：%s' % commodityGroupName)
	highLightElement(driver, acgp.save())
	acgp.save().click()
	logger.info(u'点击保存按钮')
	logger.info(u'提示信息：%s' % acgp.information())
