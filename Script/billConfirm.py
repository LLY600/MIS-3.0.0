'''
账单确认场景用例
'''

from Action.login import *
from Action.confirmBill import *
from toolKit.readExcelFile import *
from toolKit.formatTime import *
from toolKit.screenCapture import *
from toolKit.compareFile import *
from PageObject.tableDataPage import *


def test_confirm_bill():
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
				ref.getSheetByName(u'账单管理')
				sign = ref.get_start_sign(ref, u'账单确认')
				list2 = ref.cycle_index_list(ref, u'账单确认')
				for index02, row02 in enumerate(list2):
					if row02[2].value == 'Y':
						ref.writeValueToCell(dateTimeChineseFormat2(), index02 + sign + 2, 5)
						try:
							contract = row02[1].value
							get_bill_data(driver, contract)
							file1 = listData + u'confirm_bill_data.log'
							file2 = fileLibrary + u'confirm_bill_data.log'
							if contain_file(file1, file2) == '一致':
								logger.info(u'对比文件一致，请确认列表数据！')
								ref.getSheetByName(u'账单调整维护')  # 因后续（账单调整）测试需要用到账单号，这里获取后提前写入（账单调整维护）表格
								sign = ref.get_start_sign(ref, u'添加账单调整')
								gtd = GetTableData(driver)
								ref.writeValueToCell(gtd.row15(), index02 + sign + 2, 4)
								ref.getSheetByName(u'收款管理')  # 因后续（收款）测试需要用到账单号，这里获取后提前写入（收款管理）表格
								sign = ref.get_start_sign(ref, u'添加收款')
								ref.writeValueToCell(gtd.row15(), index02 + sign + 2, 6)
								confirm_bill_data(driver)
								bcp = BillConfirmPage(driver)
								if str(bcp.information()) == str(row02[3].value):
									ref.getSheetByName(u'账单管理')
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
