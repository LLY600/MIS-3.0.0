'''
单独封装login方法
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback
from FilePath.readFilePath import *
from PageObject.loginPage import *
from time import sleep
from toolKit.log import *
# import allure

def login(driver, loginId, passWord):
	driver.maximize_window()
	lp = LoginPage(driver) # 实例化
	# with allure.step('输入账号'):
	lp.getLoginId().send_keys(loginId)
	# with allure.step('输入密码'):
	lp.getPassWord().send_keys(passWord)
	# with allure.step('点击登录按钮'):
	lp.getSubmit().click()
	sleep(1)
	logger.info(u'登录账号%s' % loginId)
	logger.info(u'用户%s登录成功' % lp.userName())
	return '登录成功!'
