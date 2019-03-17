'''
添加收款功能
'''

from Action.login import *
from Action.addCollection import *
from toolKit.readExcelFile import *
from toolKit.formatTime import *
from toolKit.screenCapture import *
from toolKit.compareFile import *
from PageObject.tableDataPage import *


def test_add_collection():
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
				ref.getSheetByName(u'收款管理')
				list2 = [ref.getSingleRow(3)]
				acp = AddCollectionPage(driver)
				for index02, row02 in enumerate(list2):
					if row02[8].value == 'Y':
						ref.writeValueToCell(dateTimeChineseFormat2(), index02 + 4, 11)
						try:
							merchantName = row02[1].value
							contractName = row02[2].value
							paymentTime = str(row02[3].value)[0:10]
							settlementGroup = row02[4].value
							billNum = str(row02[5].value)
							collectionMoney = str(row02[6].value)
							deductMoney = str(row02[7].value)
							addCollection(driver, merchantName, contractName, paymentTime, settlementGroup, billNum, collectionMoney, deductMoney)
							if acp.information() == row02[9].value:
								ref.writeValueToCell('Pass', index02 + 4, 12)
							else:
								ref.writeValueToCell('Fail', index02 + 4, 12)
								screenCapture(driver)  # 保存截图
								assert False
						except:
							ref.writeValueToCell('Fail', index02 + 4, 12)
							screenCapture(driver)
							assert False
					else:
						ref.writeValueToCell('N/A', index02 + 4, 12)
						continue
					acp.informationConfirm().click()
					time.sleep(2)
					contractName = row02[2].value
					addCollectionList(driver, contractName)
					file1 = listData + u'addCollectionList.log'
					file2 = fileLibrary + u'addCollectionList.log'
					if compareFile(file1, file2) == '一致':
						logger.info(u'对比文件一致，测试通过！')
					else:
						logger.info(u'对比文件不一致，测试失败！')
					driver.refresh()
			except Exception as e:
				logger.info(u'异常信息：' + ''.join(e.args))
		else:
			ref.writeValueToCell('N/A', index01+2, 7)
			continue
	logger.info(u'---------------我是分割线---------------')
	driver.quit()
























