'''
保证金处理确认场景用例
'''

from Action.login import *
from Action.confirmMarginHandle import *
from toolKit.readExcelFile import *
from toolKit.formatTime import *
from toolKit.screenCapture import *
from toolKit.compareFile import *


def test_confirm_margin_handle():
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
				sign = ref.get_start_sign(ref, u'保证金处理确认')
				list2 = ref.cycle_index_list(ref, u'保证金处理确认')
				for index02, row02 in enumerate(list2):
					if row02[2].value == 'Y':
						ref.writeValueToCell(dateTimeChineseFormat2(), index02 + sign + 2, 5)
						try:
							contract = row02[1].value
							get_margin_handle_data(driver, contract)
							file1 = listData + u'confirm_margin_handle_data.log'
							file2 = fileLibrary + u'confirm_margin_handle_data.log'
							if contain_file(file1, file2) == '一致':
								logger.info(u'对比文件一致，请确认列表数据！')
								confirm_margin_handle_data(driver)
								mhc = MarginHandleConfirmPage(driver)
								if str(mhc.information()) == str(row02[3].value):
									ref.writeValueToCell('Pass', index02 + sign + 2, 6)
									logger.info(u'测试通过！')
								else:
									ref.writeValueToCell('Fail', index02 + sign + 2, 6)
									logger.info(u'测试失败！')
									screenCapture(driver)
									assert False
							else:
								logger.info(u'对比文件不一致，请检查列表数据！')
								screenCapture(driver)
						except:
							ref.writeValueToCell('Fail', index02 + sign + 2, 6)
							screenCapture(driver)
							assert False
						logger.info(u'<------以上是Excel表格第%s组测试数据------>' % str(index02 + 1))
						driver.refresh()
			except Exception as e:
				logger.info(u'异常信息：' + ''.join(e.args))
		else:
			ref.writeValueToCell('N/A', index01 + 2, 7)
			continue
	logger.info(u'***********该功能用例执行完毕!***********')
	driver.quit()
