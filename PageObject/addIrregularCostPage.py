# from selenium import webdriver                                #不规则费用页面对象封装
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException,NoSuchElementException
# import traceback
# from toolKit.readConfigurationFile import *
# from FilePath.readFilePath import *
# from toolKit.findElements import *

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback
from Action.login import *
from toolKit.findElements import *

class AddIrregularCostPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.readConfigurationFile = readConfigurationFile()
        self.addIrregularCost = self.readConfigurationFile.getItemSection('addIrregularCost')
    def getFinancialManagement(self):    #财务管理
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.financialManagement'.lower()].split('>')
        financialManagement = getElement(self.driver, locateType, locateExpression)
        return financialManagement
    def getIrregularCost(self):         #不规则费用管理
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.irregularCost'.lower()].split('>')
        irregularCost = getElement(self.driver, locateType, locateExpression)
        return irregularCost
    def getIrregularList(self):         #不规则费用维护
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.irregularList'.lower()].split('>')
        irregularList = getElement(self.driver, locateType, locateExpression)
        return  irregularList
    def frame(self):      #切换框架
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.frame'.lower()].split('>')
        frame = getElement(self.driver, locateType, locateExpression)
        return  frame
    def getAddIrregular(self): # 添加按钮
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.addIrregular'.lower()].split('>')
        addIrregular = getElement(self.driver, locateType, locateExpression)
        return addIrregular
    def frame2(self):      #切换框架
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.frame2'.lower()].split('>')
        frame2 = getElement(self.driver, locateType, locateExpression)
        return frame2
    def getMerchantName(self): # 商户名称
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.merchantName'.lower()].split('>')
        merchantName = getElement(self.driver, locateType, locateExpression)
        return merchantName
    def getMerchantNameSearchBox(self): # 商户名称搜索框
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.merchantNameSearchBox'.lower()].split('>')
        merchantNameSearchBox = getElement(self.driver, locateType, locateExpression)
        return merchantNameSearchBox
    def getMerchantNameSearch(self): # 商户名称搜索按钮
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.merchantNameSearch'.lower()].split('>')
        merchantNameSearch = getElement(self.driver, locateType, locateExpression)
        return merchantNameSearch
    def getMerchantNameSearchResult(self): # 选择第一个商户
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.merchantNameSearchResult'.lower()].split('>')
        merchantNameSearchResult = getElement(self.driver, locateType, locateExpression)
        return merchantNameSearchResult
    def getContractName(self): # 合同号
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.contractName'.lower()].split('>')
        contractName = getElement(self.driver, locateType, locateExpression)
        return contractName
    def getContractNameSearchBox(self): # 合同号搜索框
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.contractNameSearchBox'.lower()].split('>')
        contractNameSearchBox = getElement(self.driver, locateType, locateExpression)
        return contractNameSearchBox
    def getContractNameSearch(self): # 合同号搜索按钮
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.contractNameSearch'.lower()].split('>')
        contractNameSearch = getElement(self.driver, locateType, locateExpression)
        return contractNameSearch
    def getContractNameSearchResult(self): # 选择第一个合同
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.contractNameSearchResult'.lower()].split('>')
        contractNameSearchResult = getElement(self.driver, locateType, locateExpression)
        return contractNameSearchResult
    def getSettlementGroup(self): #结算组别
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.settlementGroup'.lower()].split('>')
        settlementGroup = getElement(self.driver, locateType, locateExpression)
        return settlementGroup
    def getSettlementGroupChoose(self): #选择第一个结算组别
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.settlementGroupChoose'.lower()].split('>')
        settlementGroupChoose = getElement(self.driver, locateType, locateExpression)
        return settlementGroupChoose
    def getAccountPayable(self): #账期
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.accountPayable'.lower()].split('>')
        accountPayable = getElement(self.driver, locateType, locateExpression)
        return accountPayable
    def getAccountPayableSearchBox(self): #账期搜索框
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.accountPayableSearchBox'.lower()].split('>')
        accountPayableSearchBox = getElement(self.driver, locateType, locateExpression)
        return accountPayableSearchBox
    def getAccountPayableSearch(self): #账期搜索按钮（ID容易发生改变）
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.accountPayableSearch'.lower()].split('>')
        accountPayableSearch = getElement(self.driver, locateType, locateExpression)
        return accountPayableSearch
    def getAccountPayableChoose(self): #选择第一个账期（ID容易发生改变）
        locateType,locateExpression = self.addIrregularCost['addIrregularCost.accountPayableChoose'.lower()].split('>')
        accountPayableChoose = getElement(self.driver, locateType, locateExpression)
        return accountPayableChoose
    def getAddCost(self):  # 增加费用信息
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.addCost'.lower()].split('>')
        addCost = getElement(self.driver, locateType, locateExpression)
        return addCost
    def getCostName(self):  #费用项目
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.costName'.lower()].split('>')
        costName = getElement(self.driver, locateType, locateExpression)
        return costName
    def getCostNameSearchBox(self):  #费用名称
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.costNameSearchBox'.lower()].split('>')
        costNameSearchBox = getElement(self.driver, locateType, locateExpression)
        return costNameSearchBox
    def getAccountPayableSearch2(self):  #费用名称搜索按钮
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.accountPayableSearch2'.lower()].split(
            '>')
        accountPayableSearch2 = getElement(self.driver, locateType, locateExpression)
        return accountPayableSearch2
    def getAccountPayableChoose2(self):  #选择第一个费用名称
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.accountPayableChoose2'.lower()].split('>')
        accountPayableChoose2 = getElement(self.driver, locateType, locateExpression)
        return accountPayableChoose2
    def getCostMoney(self):  #费用金额
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.costMoney'.lower()].split( '>')
        costMoney = getElement(self.driver, locateType, locateExpression)
        return costMoney
    def getCostMoney2(self):  #再次点击费用金额，清除文本数据
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.costMoney2'.lower()].split('>')
        costMoney2 = getElement(self.driver, locateType, locateExpression)
        return costMoney2
    def getCostMonth(self):  #费用月份
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.costMonth'.lower()].split('>')
        costMonth = getElement(self.driver, locateType, locateExpression)
        return costMonth
    def getCostMonth2(self):  #二次点击费用月份
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.costMonth2'.lower()].split('>')
        costMonth2 = getElement(self.driver, locateType, locateExpression)
        return costMonth2
    def getCostMonthChoose(self):  #选择第一个月份
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.costMonthChoose'.lower()].split('>')
        costMonthChoose = getElement(self.driver, locateType, locateExpression)
        return costMonthChoose
    def getNote(self):  #备注
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.note'.lower()].split('>')
        note = getElement(self.driver, locateType, locateExpression)
        return note
    def getNote2(self):  #二次点击备注
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.note2'.lower()].split('>')
        note2 = getElement(self.driver, locateType, locateExpression)
        return note2
    def getAddButton(self):  #添加
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.addButton'.lower()].split('>')
        addButton = getElement(self.driver, locateType, locateExpression)
        return addButton
    def information(self):
        locateType, locateExpression = self.addIrregularCost['addIrregularCost.information'.lower()].split('>')
        information = getElement(self.driver, locateType, locateExpression)
        return information.text


if __name__ =='__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://192.168.1.136:7088/')
    login(driver, 'LLY01', '123456')
    aic = AddIrregularCostPage(driver)
    aic.getFinancialManagement().click() #财务管理
    aic.getIrregularCost().click()
    aic.getIrregularList().click()
    driver.switch_to.frame(aic.frame()) #切换框架
    time.sleep(1)
    aic.getAddIrregular().click()   #添加不规则费用按钮
    driver.switch_to_default_content()
    driver.switch_to.frame(aic.frame2())  # 切换框架
    time.sleep(0.5)
    aic.getMerchantName().click()  #商户名称
    aic.getMerchantNameSearchBox().send_keys('5S压榨')
    aic.getMerchantNameSearch().click()
    aic.getMerchantNameSearchResult().click()
    aic.getContractName().click() #合同号
    aic.getContractNameSearchBox().send_keys('XCSD180921001')
    aic.getContractNameSearch().click()
    time.sleep(0.5)
    aic.getContractNameSearchResult().click()
    time.sleep(0.5)
    aic.getSettlementGroup().click()  #结算组别
    aic.getSettlementGroupChoose().click()
    aic.getAccountPayable().click()  #账期
    aic.getAccountPayableSearchBox().send_keys('201902')
    time.sleep(0.5)
    aic.getAccountPayableSearch().click()
    time.sleep(0.5)
    aic.getAccountPayableChoose().click()
    aic.getAddCost().click()   #添加费用
    aic.getCostName().click()#重复点击
    aic.getCostName().click()#重复点击
    time.sleep(0.5)
    aic.getCostNameSearchBox().send_keys('不规则费用')
    aic.getAccountPayableSearch2().click()
    time.sleep(0.5)
    aic.getAccountPayableChoose2().click()
    aic.getCostMoney().click()
    aic.getCostMoney2().clear()
    time.sleep(0.5)
    aic.getCostMoney2().send_keys('1200.00')
    aic.getCostMonth().click()  #费用月份
    aic.getCostMonth2().click()
    aic.getCostMonthChoose().click()
    time.sleep(0.5)
    aic.getNote().click()
    aic.getNote2().send_keys('备注信息')
    time.sleep(0.5)
    aic.getAddButton().click()
    time.sleep(1)
    driver.refresh()

