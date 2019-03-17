from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback
from Action.login import *

class AdvancePayment(object):
    def __init__(self,driver):
        self.driver = driver
        self.readConfigurationFile = readConfigurationFile()
        self.advanceCharge = self.readConfigurationFile.getItemSection('advanceCharge')
    def financialManagement(self):  #财务管理
        locateType,locateExpression = self.advanceCharge['advanceCharge.financialManagement'.lower()].split('>')
        financialManagement = getElement(self.driver,locateType,locateExpression)
        return financialManagement
    def abvanceCharge(self):    #预付款
        locateType,locateExpression = self.advanceCharge['advanceCharge.abvanceCharge'.lower()].split('>')
        abvanceCharge = getElement(self.driver,locateType,locateExpression)
        return abvanceCharge
    def aCMaintenance(self):    #预付款维护
        locateType,locateExpression  = self.advanceCharge['advanceCharge.aCMaintenance'.lower()].split('>')
        aCMaintenance = getElement(self.driver,locateType,locateExpression)
        return aCMaintenance
    def handoverFrame(self):    #切换框架
        locateType,locateExpression = self.advanceCharge['advanceCharge.handoverFrame'.lower()].split('>')
        handoverFrame = getElement(self.driver,locateType,locateExpression)
        return handoverFrame
    def addTo(self):        #添加预付款
        locateType, locateExpression = self.advanceCharge['advanceCharge.addTo'.lower()].split('>')
        addTo = getElement(self.driver, locateType, locateExpression)
        return addTo
    def addToHandoverFrame(self):        #切换添加中框
        locateType, locateExpression = self.advanceCharge['advanceCharge.addToHandoverFrame'.lower()].split('>')
        addToHandoverFrame = getElement(self.driver, locateType, locateExpression)
        return addToHandoverFrame
    def merchant(self):        #商户
        locateType, locateExpression = self.advanceCharge['advanceCharge.merchant'.lower()].split('>')
        merchant = getElement(self.driver, locateType, locateExpression)
        return merchant
    def merchantName(self):  # 商户名称
        locateType, locateExpression = self.advanceCharge['advanceCharge.merchantName'.lower()].split('>')
        merchantName = getElement(self.driver, locateType, locateExpression)
        return merchantName
    def merchantSearc(self):  # 商户搜索
        locateType, locateExpression = self.advanceCharge['advanceCharge.merchantSearc'.lower()].split('>')
        merchantSearc = getElement(self.driver, locateType, locateExpression)
        return merchantSearc
    def merchantSearchResult(self):  # 选择商户结果
        locateType, locateExpression = self.advanceCharge['advanceCharge.merchantSearchResult'.lower()].split('>')
        merchantSearchResult = getElement(self.driver, locateType, locateExpression)
        return merchantSearchResult
    def contractName(self):  # 合同
        locateType, locateExpression = self.advanceCharge['advanceCharge.contractName'.lower()].split('>')
        contractName = getElement(self.driver, locateType, locateExpression)
        return contractName
    def contractNameSearchBox(self):  # 合同名称
        locateType, locateExpression = self.advanceCharge['advanceCharge.contractNameSearchBox'.lower()].split('>')
        contractNameSearchBox = getElement(self.driver, locateType, locateExpression)
        return contractNameSearchBox
    def contractSearc(self):  # 搜索合同
        locateType, locateExpression = self.advanceCharge['advanceCharge.contractSearc'.lower()].split('>')
        contractSearc = getElement(self.driver, locateType, locateExpression)
        return contractSearc
    def contractSearchResulh(self):  # 合同搜索结果
        locateType, locateExpression = self.advanceCharge['advanceCharge.contractSearchResulh'.lower()].split('>')
        contractSearchResulh = getElement(self.driver, locateType, locateExpression)
        return contractSearchResulh
    def addRows(self):  # 添加行
        locateType, locateExpression = self.advanceCharge['advanceCharge.addRows'.lower()].split('>')
        addRows = getElement(self.driver, locateType, locateExpression)
        return addRows
    def receivables(self):  # 点击收款方式
        locateType, locateExpression = self.advanceCharge['advanceCharge.receivables'.lower()].split('>')
        receivables = getElement(self.driver, locateType, locateExpression)
        return receivables
    def clickReceipts(self):  # 再次点击收款方式
        locateType, locateExpression = self.advanceCharge['advanceCharge.clickReceipts'.lower()].split('>')
        clickReceipts = getElement(self.driver, locateType, locateExpression)
        return clickReceipts
    def paymentMethod(self):  # 选择收款方式
        locateType, locateExpression = self.advanceCharge['advanceCharge.paymentMethod'.lower()].split('>')
        paymentMethod = getElement(self.driver, locateType, locateExpression)
        return paymentMethod
    def amountCollected(self):  # 收款金额
        locateType, locateExpression = self.advanceCharge['advanceCharge.amountCollected'.lower()].split('>')
        amountCollected = getElement(self.driver, locateType, locateExpression)
        return amountCollected
    def inputAmount(self):  # 输入金额
        locateType, locateExpression = self.advanceCharge['advanceCharge.inputAmount'.lower()].split('>')
        inputAmount = getElement(self.driver, locateType, locateExpression)
        return inputAmount
    def peservation(self):  # 添加
        locateType, locateExpression = self.advanceCharge['advanceCharge.peservation'.lower()].split('>')
        peservation = getElement(self.driver, locateType, locateExpression)
        return peservation
    def yes(self):  # yes
        locateType, locateExpression = self.advanceCharge['advanceCharge.yes'.lower()].split('>')
        yes = getElement(self.driver, locateType, locateExpression)
        return yes
    def information(self):
        locateType, locateExpression = self.advanceCharge['advanceCharge.information'.lower()].split('>')
        information = getElement(self.driver, locateType, locateExpression)
        return information.text
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://192.168.1.136:7088')
    login(driver, 'LLY01', '123456')
    amc = AdvancePayment(driver)
    amc.financialManagement().click()
    amc.abvanceCharge().click()
    amc.aCMaintenance().click()
    driver.switch_to.frame(amc.handoverFrame())
    time.sleep(4)
    amc.addTo().click()
    driver.switch_to.default_content()
    driver.switch_to.frame(amc.addToHandoverFrame())
    time.sleep(1)
    amc.merchant().click()
    amc.merchantName().send_keys('5S压榨')
    amc.merchantSearc().click()
    amc.merchantSearchResult().click()
    time.sleep(1)
    amc.contractName().click()
    amc.contractNameSearchBox().send_keys('XCSD180921006')
    amc.contractSearc().click()
    time.sleep(1)
    amc.contractSearchResulh().click()
    time.sleep(1)
    amc.addRows().click()
    amc.receivables().click()
    time.sleep(1)
    amc.receivables().click()
    amc.paymentMethod().click()
    time.sleep(1)
    amc.amountCollected().click()
    amc.inputAmount().clear()
    time.sleep(0.5)
    amc.inputAmount().send_keys('5400')
    amc.peservation().click()
    time.sleep(0.5)
    amc.yes().click()
    time.sleep(1)















