'''
保证金处理功能
'''

from PageObject.addMarginHandlePage import *
from PageObject.tableDataPage import *
from toolKit.screenCapture import *
from toolKit.highLightElement import *
from prettytable import PrettyTable
from time import sleep

def add_margin_handle(driver, merchant='', contract='', handleType='', settlementGroup='', expenseItem='', handleDate=''
                      , marginType='', handleMoney='', paymentType='', money=''):
	mh = MarginHandlePage(driver)
	logger.info(u'测试保证金处理')
	mh.financialManagement().click()
	logger.info(u'点击财务管理')
	mh.marginManagement().click()
	logger.info(u'点击保证金管理')
	mh.marginHandle().click()
	logger.info(u'点击保证金处理')
	driver.switch_to.frame(mh.frameOfMarginHandle())
	sleep(4)
	highLightElement(driver, mh.add())
	mh.add().click()
	logger.info(u'点击添加按钮')
	driver.switch_to.default_content()
	driver.switch_to.frame(mh.frameOfAddMarginHandle())
	sleep(2)
	try:
		mh.mall().click()
		sleep(0.5)
		mh.mallSelect().click()
	except:
		pass
	mh.merchantName().click()
	sleep(0.5)
	logger.info(u'点击经营商户')
	# highLightElement(driver, mh.merchantNameInput())
	mh.merchantNameInput().send_keys(merchant)
	logger.info(u'商户名称输入%s' % merchant)
	highLightElement(driver, mh.merchantNameSearch())
	mh.merchantNameSearch().click()
	logger.info(u'点击搜索按钮')
	sleep(1)
	highLightElement(driver, mh.merchantNameResult())
	mh.merchantNameResult().click()
	logger.info(u'点击搜索结果')
	# highLightElement(driver, mh.contractName())
	mh.contractName().click()
	logger.info(u'点击合同号')
	# highLightElement(driver, mh.contractNameInput())
	mh.contractNameInput().send_keys(contract)
	logger.info(u'合同号输入%s' % contract)
	highLightElement(driver, mh.contractNameSearch())
	mh.contractNameSearch().click()
	logger.info(u'点击搜索按钮')
	sleep(1)
	highLightElement(driver, mh.contractNameResult())
	mh.contractNameResult().click()
	logger.info(u'点击搜索结果')
	mh.handleDate().click()
	mh.handleDateInput().send_keys(handleDate)
	logger.info(u'输入处理日期：%s' % handleDate)
	# highLightElement(driver, mh.handleType())
	mh.handleType().click()
	logger.info(u'点击处理方式')
	index = marginType
	if marginType == index:
		if handleType == u'转预收款':
			mh.handleTypeSelect('Advance').click()
			logger.info(u'选择转预收款')
			try:
				mh.settlementGroupBox().click()
				logger.info(u'点击结算组别')
				mh.settlementGroupInput().send_keys(settlementGroup)
				logger.info(u'输入结算组别：%s' % settlementGroup)
				highLightElement(driver, mh.settlementGroupSearch())
				mh.settlementGroupSearch().click()
				logger.info(u'点击结算组别搜索按钮')
				highLightElement(driver, mh.settlementGroupResult())
				mh.settlementGroupResult().click()
				logger.info(u'选择结算组别搜索结果')
				mh.expenseItem().click()
				logger.info(u'点击费用项目文本框')
				mh.expenseItemInput().send_keys(expenseItem)
				logger.info(u'输入费用项目：%s' % (expenseItem))
				mh.expenseItemSearch().click()
				sleep(1)
				mh.expenseItemSelect().click()
				logger.info(u'选择费用项目')
				mh.toAdvancePayment('row' + str(int(index) + 1)).click()
				sleep(0.5)
				mh.toAdvancePaymentInput('row' + str(int(index) + 1)).clear()
				sleep(1)
				mh.toAdvancePaymentInput('row' + str(int(index) + 1)).send_keys(handleMoney)
			except:
				pass
		elif handleType == u'罚没':
			mh.handleTypeSelect('Confiscate').click()
			logger.info(u'选择罚没')
			mh.toConfiscatePayment('row' + str(int(index) + 1)).click()
			mh.toConfiscatePaymentInput('row' + str(int(index) + 1)).clear()
			sleep(0.5)
			mh.toConfiscatePaymentInput('row' + str(int(index) + 1)).send_keys(handleMoney)
		else:
			mh.handleTypeSelect('Return').click()
			logger.info(u'选择归还')
			mh.toReturnPayment('row' + str(int(index) + 1)).click()
			mh.toReturnPaymentInput('row' + str(int(index) + 1)).clear()
			sleep(0.5)
			mh.toReturnPaymentInput('row' + str(int(index) + 1)).send_keys(handleMoney)
			mh.addRow().click()
			logger.info(u'点击增加行按钮')
			mh.paymentMethodBox().click()
			sleep(0.5)
			mh.paymentMethodInput().click()
			if paymentType == 'AT_支付宝':
				mh.paymentMethod('Alipay').click()
			elif paymentType == 'AT_微信':
				mh.paymentMethod('WeChat').click()
			elif paymentType == 'AT_现金':
				mh.paymentMethod('Cash').click()
			else:
				mh.paymentMethod('Card').click()
			sleep(0.5)
			logger.info(u'选择支付方式：%s' % (paymentType))
			mh.paymentBox().click()
			sleep(0.5)
			mh.paymentInput().clear()
			sleep(0.5)
			mh.paymentInput().send_keys(money)
			logger.info(u'输入收款金额：%s' % (money))
	mh.save().click()
	sleep(1)
	logger.info(u'点击添加按钮')
	logger.info(u'提示信息：%s' % mh.information())


def get_margin_handle_data(driver, contract, handleType):
	mh = MarginHandlePage(driver)
	sleep(0.5)
	mh.confirm().click()
	driver.switch_to.default_content()
	driver.switch_to.frame(mh.frameOfMarginHandle())
	sleep(2)
	mh.contractName().click()
	sleep(0.5)
	mh.contractNameInput1().send_keys(contract)
	mh.contractNameSearch1().click()
	sleep(0.5)
	mh.contractNameResult1().click()
	mh.handleType().click()
	sleep(0.5)
	if handleType == '转预收款':
		mh.handleType2('ToAdvance').click()
	elif handleType == '罚没':
		mh.handleType2('ToConfiscate').click()
	else:
		mh.handleType2('ToReturn').click()
	mh.search().click()
	sleep(2)
	fileName = listData + 'add_margin_handle_data.log'
	table = PrettyTable(['购物中心', '状态', '合同号', '经营商户', '处理时间', '处理金额', '处理方式'])
	table.align['购物中心'] = '1'
	table.padding_width = 1
	gtd = GetTableData(driver)
	table.add_row([gtd.row15(), gtd.row16(), gtd.row17(), gtd.row18(), gtd.row19(), gtd.row110(), gtd.row111()])
	logger.info(u'正在获取列表数据')
	time.sleep(1)
	print(table)
	with open(fileName, 'w') as file:
		file.write(str(table))
		file.write('\n')
	logger.info(u'保存位置:%s' % fileName)