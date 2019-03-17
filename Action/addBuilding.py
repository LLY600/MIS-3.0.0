'''
封装添加楼宇独立功能
'''

from PageObject.addBuildingPage import *
from toolKit.highLightElement import *
from toolKit.handleKey import *



def addBuilding(driver, buildingNum='', buildingName='', area='', isBuilding=''):
	abp = AddBuildingPage(driver)
	logger.info(u'测试添加楼宇')
	abp.tenancyManagement().click()
	logger.info(u'点击租务管理')
	abp.propertyManagement().click()
	logger.info(u'点击资产管理')
	abp.buildingManagement().click()
	logger.info(u'点击楼宇管理')
	driver.switch_to.frame(abp.frameOfBuildingManagement())
	time.sleep(4)
	highLightElement(driver, abp.selectMall())
	abp.selectMall().click()
	logger.info(u'选择购物中心')
	highLightElement(driver, abp.add())
	abp.add().click()
	logger.info(u'点击添加按钮')
	handleAlert(2, 'enter')  # 处理flash
	time.sleep(1.5)
	driver.switch_to.frame(abp.frameOfAddBuilding())
	highLightElement(driver, abp.buildingNumBox())
	abp.buildingNumBox().click()
	abp.buildingNum().send_keys(buildingNum)
	logger.info(u'输入物业性质编码：%s' % buildingNum)
	highLightElement(driver, abp.buildingNameBox())
	abp.buildingNameBox().click()
	abp.buildingName().send_keys(buildingName)
	logger.info(u'输入物业性质编码：%s' % buildingName)
	highLightElement(driver, abp.buildingTypeBox())
	abp.buildingType().click()
	logger.info(u'点击楼宇类型文本框')
	abp.buildingTypeSelect().click()
	logger.info(u'选择楼宇类型')
	highLightElement(driver, abp.isBuildingBox())
	abp.isBuilding().click()
	logger.info(u'点击是否是楼宇文本框')
	if isBuilding == '是':
		highLightElement(driver, abp.isBuildingSelect1())
		abp.isBuildingSelect1().click()
	else:
		highLightElement(driver, abp.isBuildingSelect2())
		abp.isBuildingSelect2().click()
	logger.info(u'选择楼宇:%s' % (isBuilding))
	highLightElement(driver, abp.areaBox())
	abp.area().send_keys(area)
	logger.info(u'输入楼宇面积：%s' % area)
	highLightElement(driver, abp.save())
	abp.save().click()
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % abp.information())
