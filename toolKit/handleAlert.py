'''
封装操作页面falsh，不够稳定，偶尔会操作失败
'''

import time
from toolKit.log import *

def handleAlert(driver):
	try:
		alert = driver.switch_to.alert
		time.sleep(3)
		# assert alert.text == '您未安装FLASH控件，无法上传图片！请安装FLASH控件后再试。'
		while not alert.text == '':
			alert.accept()
	except:
		logger.info(u'Flash弹窗已确认，继续执行')
