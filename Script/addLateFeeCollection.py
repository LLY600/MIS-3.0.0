'''
添加滞纳金收款功能
'''
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback
from Action.login import *
from Action.addLateFeeCollection import *
from toolKit.readExcelFile import *
from FilePath.readFilePath import *
from toolKit.log import *
from toolKit.formatTime import *
from toolKit.screenCapture import *
from toolKit.compareFile import *


def test_add_LateFee_collection():
	'''
	用例描述：测试滞纳金收款功能。
	'''
	driver = webdriver.Chrome()
	ref = ReadExcelFile(excelDataPath)
	ref.getSheetByName(u'登录地址账号')
	list1 = ref.getAllRows()[1:]
	for index01, row01 in enumerate(list1):
		driver.maximize_window()
		if row01[4].value == 'Y':
			driver.get(str(row01[1].value))
			ref.writeValueToCell(dateTimeChineseFormat2(), index01 + 2, 6)
			loginId = row01[2].value
			password = row01[3].value
			try:
				assert login(driver, loginId, password) == '登录成功!', '登录失败！'
				ref.writeValueToCell('Pass', index01 + 2, 7)
				ref.getSheetByName(u'滞纳金管理')
				list2 = [ref.getSingleRow(3)]
				alfcp = AddLateFeeCollectionPage(driver)
				for index02, row02 in enumerate(list2):
					if row02[7].value == 'Y':
						ref.writeValueToCell(dateTimeChineseFormat2(), index02 + 4, 10)
						try:
							merchantName = row02[1].value
							contractName = row02[2].value
							lateFeeNum = row02[3].value.replace('Fk', 'ZNJ')  # 将收款返回的收款单编号前缀FK替换为ZNJ
							paymentTime = str(row02[4].value)[0:10]
							collectionMoney = str(row02[5].value)
							deductMoney = str(row02[6].value)
							addLateFeeCollection(driver, merchantName, contractName, lateFeeNum, paymentTime, collectionMoney, deductMoney)
							if alfcp.information() == row02[8].value:
								ref.writeValueToCell('Pass', index02 + 4, 11)
							else:
								ref.writeValueToCell('Fail', index02 + 4, 11)
								screenCapture(driver)  # 保存截图
						except:
							ref.writeValueToCell('Fail', index02 + 4, 11)
							time.sleep(2)
							screenCapture(driver)  # 保存截图
					else:
						ref.writeValueToCell('N/A', index02 + 4, 11)
						continue
					alfcp.informationConfirm().click()
					time.sleep(2)
					contractName = row02[2].value
					addLateFeeCollectionList(driver, contractName)
					file1 = listData + u'addLateFeeCollectionList.log'
					file2 = fileLibrary + u'addLateFeeCollectionList.log'
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
























