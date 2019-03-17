'''
保证金处理场景用例
'''

from Action.login import *
from Action.addMarginHandle import *
from toolKit.readExcelFile import *
from toolKit.formatTime import *
from toolKit.screenCapture import *
from toolKit.compareFile import *


def test_add_margin_handle():
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
				sign = ref.get_start_sign(ref, u'保证金处理')
				list2 = ref.cycle_index_list(ref, u'保证金处理')
				for index02, row02 in enumerate(list2):
					if row02[11].value == 'Y':
						ref.writeValueToCell(dateTimeChineseFormat2(), index02 + sign + 2, 14)
						try:
							merchant = row02[1].value
							contract = row02[2].value
							handleType = row02[3].value
							settlementGroup = row02[4].value
							expenseItem = row02[5].value
							handleDate = str(row02[6].value)[0:10]
							marginType = str(row02[7].value)
							handleMoney = str(row02[8].value)
							paymentType = row02[9].value
							money = str(row02[10].value)
							add_margin_handle(driver, merchant, contract, handleType, settlementGroup, expenseItem,
							                  handleDate, marginType, handleMoney, paymentType, money)
							mh = MarginHandlePage(driver)
							if mh.information() == str(row02[12].value):
								ref.writeValueToCell('Pass', index02 + sign + 2, 15)
								get_margin_handle_data(driver, contract, handleType)
								file1 = listData + u'add_margin_collection_data.log'
								file2 = fileLibrary + u'add_margin_collection_data.log'
								if contain_file(file1, file2) == '一致':
									logger.info(u'对比文件一致，测试通过！')
								else:
									logger.info(u'对比文件不一致，测试失败！')
									screenCapture(driver)
							else:
								ref.writeValueToCell('Fail', index02 + sign + 2, 15)
								screenCapture(driver)
								assert False
						except:
							ref.writeValueToCell('Fail', index02 + sign + 2, 15)
							screenCapture(driver)
						logger.info(u'<------以上是Excel表格第%s组测试数据------>' % str(index02 + 1))
						driver.refresh()
					else:
						ref.writeValueToCell('N/A', index02 + sign + 2, 15)
			except Exception as e:
				logger.info(u'异常信息：' + ''.join(e.args))
		else:
			ref.writeValueToCell('N/A', index01 + 2, 7)
	logger.info(u'***********该功能用例执行完毕!***********')
	driver.quit()
