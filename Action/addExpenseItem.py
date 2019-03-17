'''
封装添加费用项目
'''

from time import sleep
from PageObject.addExpenseItemPage import *
from PageObject.tableDataPage import *
from toolKit.log import *
from toolKit.highLightElement import *
from prettytable import PrettyTable


def add_expense_item(driver, expenseItemNum='', expenseItemName='', settlementGroupName='', expenseType=''):
	aeip = AddExpenseItemPage(driver)
	logger.info(u'测试添加结算组别')
	aeip.tenancyManagement().click()
	logger.info(u'点击财务管理')
	aeip.basicSetting().click()
	logger.info(u'点击基础设置')
	aeip.expenseItemManagement().click()
	logger.info(u'点击费用项目管理')
	driver.switch_to.frame(aeip.frameOfExpenseItemManagement())
	sleep(4)
	highLightElement(driver, aeip.add())
	aeip.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.frame(aeip.frameOfAddExpenseItem())
	sleep(2)
	highLightElement(driver, aeip.expenseItemNumBox())
	aeip.expenseItemNum().send_keys(expenseItemNum)
	logger.info(u'输入费用项目编码：%s' % expenseItemNum)
	highLightElement(driver, aeip.expenseItemNameBox())
	aeip.expenseItemName().send_keys(expenseItemName)
	logger.info(u'输入费用项目名称：%s' % expenseItemName)
	highLightElement(driver, aeip.settlementGroupNameBox())
	aeip.settlementGroupName().click()
	# 如果有多个结算组别（这里仅写了2个组别，目测够用），需在如下继续添加elif判断，并在.ini配置文件配置定位表达式
	if settlementGroupName == 'AT_SettleGroupName01':
		highLightElement(driver, aeip.settlementGroupNameSelect1())
		aeip.settlementGroupNameSelect1().click()
	else:
		highLightElement(driver, aeip.settlementGroupNameSelect2())
		aeip.settlementGroupNameSelect2().click()
	logger.info(u'选择结算组别：%s' % settlementGroupName)
	highLightElement(driver, aeip.expenseTypeBox())
	aeip.expenseType().click()
	if expenseType == "固定租金":
		highLightElement(driver, aeip.expenseTypeSelect1())
		aeip.expenseTypeSelect1().click()
	elif expenseType == "提成租金":
		highLightElement(driver, aeip.expenseTypeSelect2())
		aeip.expenseTypeSelect2().click()
	elif expenseType == "保证金":
		highLightElement(driver, aeip.expenseTypeSelect3())
		aeip.expenseTypeSelect3().click()
	elif expenseType == "能耗费用":
		highLightElement(driver, aeip.expenseTypeSelect4())
		aeip.expenseTypeSelect4().click()
	elif expenseType == "不规则费用":
		highLightElement(driver, aeip.expenseTypeSelect5())
		aeip.expenseTypeSelect5().click()
	else:
		highLightElement(driver, aeip.expenseTypeSelect6())
		aeip.expenseTypeSelect6().click()
	logger.info(u'选择费用类型：%s' % expenseType)
	sleep(1)
	highLightElement(driver, aeip.save())
	aeip.save().click()
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % aeip.information())


def get_expense_item(driver, expenseItemNum=''):
	aeip = AddExpenseItemPage(driver)
	aeip.confirm().click()
	sleep(1)
	driver.switch_to.default_content()
	driver.switch_to.frame(aeip.frameOfExpenseItemManagement())
	aeip.expenseItemNum().send_keys(expenseItemNum)
	aeip.search().click()
	sleep(2)
	gtd = GetTableData(driver)
	fileName = listData + 'add_expense_item.log'
	table = PrettyTable(['费用项目编号', '费用项目名称', '结算组别名称', '费用类型名称'])
	table.align['店铺名称'] = '1'
	table.padding_width = 1
	table.add_row([gtd.row14(), gtd.row15(), gtd.row16(), gtd.row17()])
	logger.info(u'正在获取列表数据')
	sleep(2)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'保存位置:%s' % fileName)