'''
添加保证金收取场景用例
'''

from Action.login import *
from Action.addMarginCollection import *
from toolKit.readExcelFile import *
from toolKit.formatTime import *
from toolKit.screenCapture import *
from toolKit.compareFile import *
# import allure

def test_add_margin_collection():

	# 以下代码注释部分为allure报告配置，可暂时忽略！
	# allure.environment(Version='MIS 3.0 标准版')
	# allure.environment(EnvironmentAddress='http://gowins.imwork.net:7088/')
	# allure.environment(Browser='chrome')

	driver = webdriver.Chrome()
	ref = ReadExcelFile(excelDataPath)
	ref.getSheetByName(u'登录地址账号')
	list1 = ref.getAllRows()[1:]
	for index01, row01 in enumerate(list1):
		if row01[4].value == 'Y':
			driver.get(str(row01[1].value))
			ref.writeValueToCell(dateTimeChineseFormat2(), index01 + 2, 6)
			loginId = row01[2].value
			password = row01[3].value
			try:
				assert login(driver, loginId, password) == '登录成功!', '登录失败！'
				ref.writeValueToCell('Pass', index01 + 2, 7)
				ref.getSheetByName(u'保证金管理')
				sign = ref.get_start_sign(ref, u'保证金收取')
				list2 = ref.cycle_index_list(ref, u'保证金收取')
				for index02, row02 in enumerate(list2):
					if row02[10].value == 'Y':
						# 如下的数字13让人很懵逼，按照Excel表格推算应该在12列，但这里改为12的话程序会将数据写到11列，所以改为13
						ref.writeValueToCell(dateTimeChineseFormat2(), index02 + sign + 2, 13)
						try:
							merchant = row02[1].value
							contract = row02[2].value
							paymentTime = str(row02[3].value)[0:10]
							feeItem = row02[4].value
							currentPaymentMoney = str(row02[5].value)
							deposit = row02[6].value
							type = str(row02[7].value)
							paymentType = row02[8].value
							paymentMoney = str(row02[9].value)

							# allure.attach('商户名称', merchantName)
							# allure.attach('合同名称', contractName)
							# allure.attach('收款日期', paymentTime)
							# allure.attach('本次收款金额', currentPaymentMoney)
							# allure.attach('收款金额', paymentMoney)

							add_margin_collection_data(driver, merchant, contract, paymentTime, feeItem,
							currentPaymentMoney, paymentMoney, deposit, type, paymentType)
							amc = AddMarginCollectionPage(driver)
							if amc.information() == row02[11].value:
								ref.writeValueToCell('Pass', index02 + sign + 2, 14)
								get_margin_collection_data(driver, contract)
								file1 = listData + u'add_margin_collection_data.log'
								file2 = fileLibrary + u'add_margin_collection_data.log'
								if contain_file(file1, file2) == '一致':
									logger.info(u'对比文件一致，测试通过！')
								else:
									logger.info(u'对比文件不一致，测试失败！')
									screenCapture(driver)
							else:
								ref.writeValueToCell('Fail', index02 + sign + 2, 14)
								screenCapture(driver)
								assert False
						except:
							ref.writeValueToCell('Fail', index02 + sign + 2,  14)
							screenCapture(driver)
						logger.info(u'<------以上是Excel表格第%s组测试数据------>' % str(index02 + 1))
						driver.refresh()
					else:
						ref.writeValueToCell('N/A', index02 + sign + 2,  14)
			except Exception as e:
				logger.info(u'异常信息：' + ''.join(e.args))
		else:
			ref.writeValueToCell('N/A', index01 + 2, 7)
			continue
	logger.info(u'***********该功能用例执行完毕!***********')
	driver.quit()
























