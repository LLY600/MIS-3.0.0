'''
调整费用添加做数据框架
'''
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback

from Action.addAdustmentFee import *
from toolKit.readExcelFile import *
from FilePath.readFilePath import *
from toolKit.log import *
from toolKit.formatTime import *
from toolKit.screenCapture import *

#定义
def addAdustmentFee():
		ref = ReadExcelFile(excelDataPath)
		ref.getSheetByName(u'登录账号')
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get('http://192.168.1.136:7088/')
		ref = ReadExcelFile(excelDataPath)
		ref.getSheetByName(u'登录账号')
		rows_login = ref.getAllRows()[1:]  # row行,去掉第一行标题数据
		for index01, row01 in enumerate(rows_login):  # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标,此处下标用index表示
			if row01[3].value == 'Y':
				loginId = row01[1].value
				password = row01[2].value
				try:
					login(driver, loginId, password)
					ref.getSheetByName(u'添加调整费用')
					rows_addAdustment = ref.getAllRows()[1:]
					for index02, row02 in enumerate(rows_addAdustment):
						if row02[6].value == 'Y':
							try:
								ChooseMerchantDate = row02[1].value
								SearchContract = row02[2].value
								SearchAccount = str(row02[3].value)
								ClickFeeSear = str(row02[4].value)
								ClickCurrAdjustment1 = str(row02[5].value)
								logger.info(u'【第%s组测试数据】' % (index02 + 1))
								addAdustmentFeeModule(driver, ChooseMerchantDate, SearchContract, SearchAccount, ClickFeeSear, ClickCurrAdjustment1)
								afa = AdustmentFeeAdd(driver)
								if str(afa.information()) == str(row02[7].value):
									ref.writeValueToCell('Pass', index02+2,  10)
									logger.info(u'测试通过！')
								else:
									ref.writeValueToCell('Fail', index02 + 2, 10)
									logger.info(u'测试失败！')
									screenCapture(driver)  # 保存截图
								ref.writeValueToCell(dateTimeChineseFormat2(), index02 + 2, 9)
							except:
								ref.writeValueToCell('Fail', index02+2,  10)
								ref.writeValueToCell(dateTimeChineseFormat2(), index02 + 2, 9)
								time.sleep(5)
								screenCapture(driver)
						else:
							ref.writeValueToCell('N/A', index02+2,  10)
							continue
						ref.writeValueToCell(dateTimeChineseFormat2(), index02 + 2, 9)
						time.sleep(2)
						driver.refresh()

				except Exception as e:
					ref.getSheetByName(u'登录账号')
					ref.writeValueToCell('Fail', index01+2, 6)
					ref.writeValueToCell(dateTimeChineseFormat2(), index01+2, 5)
					logger.info(u'异常信息：' + ''.join(e.args))

				ref.getSheetByName(u'登录账号')
				ref.writeValueToCell('Pass', index01 + 2, 6)
				ref.writeValueToCell(dateTimeChineseFormat2(), index01 + 2, 5)
			else:
				ref.getSheetByName(u'登录账号')
				ref.writeValueToCell('N/A', index01+2, 6)
			continue
		logger.info(u'---------------我是分割线---------------')
		driver.quit()
