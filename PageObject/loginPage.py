'''
登录页面对象
'''

from toolKit.readConfigurationFile import *
from toolKit.findElements import *

class LoginPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10, 0.2)  # 显示等待
		self.readConfigurationFile = readConfigurationFile()  # 获取配置文件信息
		self.loginPageItems = self.readConfigurationFile.getItemSection('loginPage')
	def getLoginId(self):
		locateType, locateExpression = self.loginPageItems['loginPage.loginId'.lower()].split('>')
		loginId =getElement(self.driver, locateType, locateExpression)
		return loginId
	def getPassWord(self):
		locateType, locateExpression = self.loginPageItems['loginPage.passWord'.lower()].split('>')
		passWord = getElement(self.driver, locateType, locateExpression)
		return passWord
	def getSubmit(self):
		locateType, locateExpression = self.loginPageItems['loginPage.submit'.lower()].split('>')
		submit = getElement(self.driver, locateType, locateExpression)
		return submit
	def userName(self):
		locateType, locateExpression = self.loginPageItems['loginPage.userName'.lower()].split('>')
		userName = getElement(self.driver, locateType, locateExpression)
		return userName.text