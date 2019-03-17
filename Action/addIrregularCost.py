'''
单独封装添加不规则费用
'''

from selenium import webdriver
from PageObject.addIrregularCostPage import *
from toolKit.log import *
from Action.login import *


def addIrregularCostModule(driver,merchantName='',contractId='',accountPayable='',costName='',money='', note=''):
    driver.implicitly_wait(5)
    aic = AddIrregularCostPage(driver)
    aic.getFinancialManagement().click()  # 财务管理
    logger.info(u'点击财务管理')
    aic.getIrregularCost().click()
    logger.info(u'点击不规则费用维护')
    aic.getIrregularList().click()
    logger.info(u'点击不规则费用')
    driver.switch_to.frame(aic.frame())  # 切换框架
    time.sleep(4)
    aic.getAddIrregular().click()  # 添加不规则费用按钮
    logger.info(u'点击添加按钮')
    driver.switch_to_default_content()
    driver.switch_to.frame(aic.frame2())  # 切换框架
    time.sleep(1)
    aic.getMerchantName().click()  # 商户名称
    time.sleep(0.5)
    aic.getMerchantNameSearchBox().send_keys(merchantName)
    logger.info(u'输入商户名称：%s' % merchantName)
    aic.getMerchantNameSearch().click()
    time.sleep(1)
    aic.getMerchantNameSearchResult().click()
    time.sleep(0.5)
    aic.getContractName().click()  # 合同号
    time.sleep(0.5)
    aic.getContractNameSearchBox().send_keys(contractId)
    time.sleep(0.5)
    logger.info(u'输入合同号：%s' % contractId)
    aic.getContractNameSearch().click()
    time.sleep(0.5)
    aic.getContractNameSearchResult().click()
    time.sleep(0.5)
    aic.getSettlementGroup().click()  # 结算组别
    aic.getSettlementGroupChoose().click()
    aic.getAccountPayable().click()  # 账期
    aic.getAccountPayableSearchBox().send_keys(accountPayable)
    logger.info(u'输入账期:%s' % accountPayable)
    time.sleep(0.5)
    aic.getAccountPayableSearch().click()
    time.sleep(1)
    aic.getAccountPayableChoose().click()
    time.sleep(0.5)
    aic.getAddCost().click()  # 添加费用
    time.sleep(0.5)
    logger.info(u'点击添加费用按钮')
    aic.getCostName().click()  # 重复点击
    time.sleep(0.5)
    aic.getCostName().click()  # 重复点击
    time.sleep(0.5)
    aic.getCostNameSearchBox().send_keys(costName)
    logger.info(u'输入费用项目：%s' % costName)
    aic.getAccountPayableSearch2().click()
    time.sleep(0.5)
    aic.getAccountPayableChoose2().click()
    aic.getCostMoney().click()
    aic.getCostMoney2().clear()
    time.sleep(0.5)
    aic.getCostMoney2().send_keys(money)
    logger.info(u'输入金额：%s' % money)
    aic.getCostMonth().click()  # 费用月份
    aic.getCostMonth2().click()
    aic.getCostMonthChoose().click()
    time.sleep(0.5)
    aic.getNote().click()
    aic.getNote2().send_keys(note)
    logger.info(u'输入备注：%s' % note)
    time.sleep(0.5)
    aic.getAddButton().click()





if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://192.168.1.136:7088/')
    login(driver, 'LLY01', '123456')
    addIrregularCostModule(driver, merchantName='5S压榨', contractId='XCSD180921001', accountPayable='201902', costName='不规则费用', money='1200.00', note='备注信息')
