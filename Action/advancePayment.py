'''
单独封装添加预收款
'''

from selenium import webdriver
from PageObject.advancePaymentPage import *
from toolKit.log import *
import time

def advancePaymentModule(driver, merchantName='', contractName='', amount=''):
    driver.implicitly_wait(5)
    ap = AdvancePayment(driver)
    logger.info(u'测试添加预收款')  #uniform
    ap.financialManagement().click()
    logger.info(u'点击财务管理')
    ap.abvanceCharge().click()
    ap.aCMaintenance().click()
    driver.switch_to.frame(ap.handoverFrame())
    time.sleep(1)
    ap.addTo().click()
    driver.switch_to.default_content()
    driver.switch_to.frame(ap.addToHandoverFrame())
    time.sleep(1)
    ap.merchant().click()
    ap.merchantName().send_keys(merchantName)
    logger.info(u'输入商户名称：%s' % merchantName)
    ap.merchantSearc().click()
    ap.merchantSearchResult().click()
    time.sleep(1)
    ap.contractName().click()
    ap.contractNameSearchBox().send_keys(contractName)
    logger.info(u'输入合同名称：%s' % contractName)
    ap.contractSearc().click()
    time.sleep(1)
    ap.contractSearchResulh().click()
    time.sleep(1)
    ap.addRows().click()
    ap.receivables().click()
    time.sleep(1)
    ap.clickReceipts().click()
    time.sleep(1)
    ap.paymentMethod().click()
    time.sleep(0.5)
    ap.amountCollected().click()
    ap.inputAmount().clear()
    time.sleep(0.5)
    ap.inputAmount().send_keys(amount)
    logger.info(u'输入收款金额：%s' % amount)
    ap.peservation().click()
    time.sleep(0.5)
    ap.yes().click()
    time.sleep(0.5)
    logger.info(u'提示信息：%s' %ap.information())

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://192.168.1.136:7088/')
    login(driver, 'LLY01', '123456')
    advancePaymentModule(driver, merchantName='5S压榨', contractName='XCSD180921006', amount='5000')
