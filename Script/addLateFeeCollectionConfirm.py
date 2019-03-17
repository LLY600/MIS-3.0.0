'''
滞纳金收款确认
'''

from Action.login import *
from Action.confirmLateFeeCollection import *
from toolKit.readExcelFile import *
from toolKit.formatTime import *
from toolKit.screenCapture import *
from toolKit.compareFile import *


def test_confirm_lateFee_collection():
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
				ref.getSheetByName(u'滞纳金管理')
				list2 = [ref.getSingleRow(7)]
				alfccp = AddLateFeeCollectionConfirmPage(driver)
				for index02, row02 in enumerate(list2):
					if row02[2].value == 'Y':
						ref.writeValueToCell(dateTimeChineseFormat2(), index02 + 8, 5)
						try:
							contractName = row02[1].value
							lateFeeCollectionConfirmList(driver, contractName)  # 获取列表数据，后续进行对比
							file1 = listData + u'lateFeeCollectionConfirmList.log'
							file2 = fileLibrary + u'lateFeeCollectionConfirmList.log'
							if compareFile(file1, file2) == '一致':
								logger.info(u'对比文件一致，请确认列表数据！')
								lateFeeCollectionConfirmSelect(driver)  # 对比一致后，确认列表数据
								if str(alfccp.information()) == str(row02[3].value):
									ref.writeValueToCell('Pass', index02 + 8, 6)
									logger.info(u'测试通过！')
								else:
									ref.writeValueToCell('Fail', index02 + 8, 6)
									logger.info(u'测试失败！')
									screenCapture(driver)
							else:
								logger.info(u'对比文件不一致，请检查列表数据！')
						except:
							ref.writeValueToCell('Fail', index02 + 8, 6)
							time.sleep(2)
							screenCapture(driver)
			except Exception as e:
				logger.info(u'异常信息：' + ''.join(e.args))
		else:
			ref.writeValueToCell('N/A', index01 + 2, 7)
			continue
	logger.info(u'---------------我是分割线---------------')
	driver.quit()
