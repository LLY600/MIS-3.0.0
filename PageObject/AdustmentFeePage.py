import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback
from Action.login import *

class AdustmentFeeAdd(object):
    def __init__(self, driver):
        self.driver = driver
        self.readConfigurationFile = readConfigurationFile()
        self.addAdustmentFee = self.readConfigurationFile.getItemSection('Adustment')
    def financialManagement(self): #点击财务管理模块
        locateType, locateExpression = self.addAdustmentFee['Adustment.FinancialManagement'.lower()].split('>')
        financialManagement = getElement(self.driver, locateType, locateExpression)
        return financialManagement
    def AdustmentFeeMangment(self): #点击调整费用管理
        locateType, locateExpression = self.addAdustmentFee['Adustment.AdustmentFeeMangment'.lower()].split('>')
        AdustmentFeeMangment=getElement(self.driver,locateType,locateExpression)
        return AdustmentFeeMangment
    def AdustmentFeeMaintain(self): #点击调整维护列表
        locateType, locateExpression = self.addAdustmentFee['Adustment.AdustmentFeeMaintain'.lower()].split('>')
        AdustmentFeeMaintain = getElement(self.driver, locateType, locateExpression)
        return AdustmentFeeMaintain
    def AdustmentFramList(self): #切换到调整费用框架
        locateType, locateExpression = self.addAdustmentFee['Adustment.fram'.lower()].split('>')
        AdustmentFramList = getElement(self.driver, locateType, locateExpression)
        return AdustmentFramList
    def CliAdustmentAddBut(self): #点击调整费用添加按钮
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickAdustmentFeeBut'.lower()].split('>')
        CliAdustmentAddBut = getElement(self.driver, locateType, locateExpression)
        return CliAdustmentAddBut
    def AdustmentAdcover(self): #切换添加数据框架
        locateType, locateExpression = self.addAdustmentFee['Adustment.frame1'.lower()].split('>')
        AdustmentAdcover = getElement(self.driver, locateType, locateExpression)
        return AdustmentAdcover
    def MallBox(self): #定位购物中心的Box
        locateType, locateExpression = self.addAdustmentFee['Adustment.ChooseMallCenter'.lower()].split('>')
        MallBox = getElement(self.driver, locateType, locateExpression)
        return MallBox
    def ChooseMallData(self): #选择购物中心数据
        locateType, locateExpression = self.addAdustmentFee['Adustment.Mall'.lower()].split('>')
        ChooseMallData = getElement(self.driver, locateType, locateExpression)
        return ChooseMallData
    def MerchantBox(self):  # 定位商户Box
        locateType, locateExpression = self.addAdustmentFee['Adustment.ChooseMerchant'.lower()].split('>')
        MerchantBox = getElement(self.driver, locateType, locateExpression)
        return MerchantBox
    def ChooseMerchantDate(self):  # 选择商户数据
        locateType, locateExpression = self.addAdustmentFee['Adustment.Merchant'.lower()].split('>')
        ChooseMerchantDate = getElement(self.driver, locateType, locateExpression)
        return ChooseMerchantDate
    def ClikcMerSearBut(self):  # 点击商户搜索按钮
        locateType, locateExpression = self.addAdustmentFee['Adustment.SearchBut'.lower()].split('>')
        ClikcMerSearBut = getElement(self.driver, locateType, locateExpression)
        return ClikcMerSearBut
    def MerchantResult(self):#得到商户数据
        locateType, locateExpression = self.addAdustmentFee['Adustment.MerchantResult'.lower()].split('>')
        MerchantResult = getElement(self.driver, locateType, locateExpression)
        return MerchantResult
    def ClickContractBox(self):#定位合同Box
        locateType, locateExpression = self.addAdustmentFee['Adustment.ChooseContract'.lower()].split('>')
        ClickContractBox = getElement(self.driver, locateType, locateExpression)
        return ClickContractBox
    def SearchContract(self):#合同输入框,搜索合同
        locateType, locateExpression = self.addAdustmentFee['Adustment.SearchContract'.lower()].split('>')
        SearchContract = getElement(self.driver, locateType, locateExpression)
        return SearchContract
    def ClickContractSearBut(self):#点击搜索合同按钮，返回搜索结果
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickSeaConBut'.lower()].split('>')
        ClickContractSearBut = getElement(self.driver, locateType, locateExpression)
        return ClickContractSearBut
    def ClickContractResult(self):#点击商户合同结果
        locateType, locateExpression = self.addAdustmentFee['Adustment.ContractResult'.lower()].split('>')
        ClickContractResult = getElement(self.driver, locateType, locateExpression)
        return ClickContractResult
    def ClickSettGroupBox(self):#定位合同组别的Box
        locateType, locateExpression = self.addAdustmentFee['Adustment.ChoosSettlementGroup'.lower()].split('>')
        ClickSettGroupBox = getElement(self.driver, locateType, locateExpression)
        return ClickSettGroupBox
    def ChooseGroupInfo(self):#选择组别信息
        locateType, locateExpression = self.addAdustmentFee['Adustment.SettlementGroup'.lower()].split('>')
        ChooseGroupInfo = getElement(self.driver, locateType, locateExpression)
        return ChooseGroupInfo
    def AccoutBox(self):#定位账期Box
        locateType, locateExpression = self.addAdustmentFee['Adustment.ChooseAccount'.lower()].split('>')
        AccoutBox = getElement(self.driver, locateType, locateExpression)
        return AccoutBox
    def AccoutSearBox(self):#点击账期搜索框
        locateType, locateExpression = self.addAdustmentFee['Adustment.SearchBOX'.lower()].split('>')
        AccoutSearBox = getElement(self.driver, locateType, locateExpression)
        return AccoutSearBox
    def SearchAccount(self):#点击输入账期的值
        locateType, locateExpression = self.addAdustmentFee['Adustment.SearchAccount'.lower()].split('>')
        SearchAccount = getElement(self.driver, locateType, locateExpression)
        return SearchAccount
    def SearchAccountBut(self):  # 点击账期搜索按钮
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickSearchBut'.lower()].split('>')
        SearchAccountBut = getElement(self.driver, locateType, locateExpression)
        return SearchAccountBut
    def ClickAccountResu(self):  # 点击账期结果
        locateType, locateExpression = self.addAdustmentFee['Adustment.RusultAccount'.lower()].split('>')
        ClickAccountResu = getElement(self.driver, locateType, locateExpression)
        return ClickAccountResu
    def ClickAddFeeInfo(self):  # 点击添加费用信息
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickAddFeeInfo'.lower()].split('>')
        ClickAddFeeInfo = getElement(self.driver, locateType, locateExpression)
        return ClickAddFeeInfo
    def ClickAddFeeBox(self):  # 点击费用项目BOX
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickFeePBox'.lower()].split('>')
        ClickAddFeeBox = getElement(self.driver, locateType, locateExpression)
        return ClickAddFeeBox
    def ClickFeePBox1(self):  # 点击费用项目数据
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickFeePBox1'.lower()].split('>')
        ClickFeePBox1 = getElement(self.driver, locateType, locateExpression)
        return ClickFeePBox1
    def ClickFeeSear(self):  # 点击费用项目搜索
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickFeeSear'.lower()].split('>')
        ClickFeeSear = getElement(self.driver, locateType, locateExpression)
        return ClickFeeSear
    def ClickSFeeSearBut(self):  # 点击费用项目搜索按钮
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickSFeeSearBut'.lower()].split('>')
        ClickSFeeSearBut = getElement(self.driver, locateType, locateExpression)
        return ClickSFeeSearBut
    def ClickSFeeResu(self):  # 点击费用项目结果数据
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickSFeeResult'.lower()].split('>')
        ClickSFeeResu = getElement(self.driver, locateType, locateExpression)
        return ClickSFeeResu
    def FeeMonthBox(self):  # 定位费用月份Box
        locateType, locateExpression = self.addAdustmentFee['Adustment.FeeMonthBox'.lower()].split('>')
        FeeMonthBox = getElement(self.driver, locateType, locateExpression)
        return FeeMonthBox
    def ClickFeeMonth(self):  # 定位输入框
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickFeeMonth'.lower()].split('>')
        ClickFeeMonth = getElement(self.driver, locateType, locateExpression)
        return ClickFeeMonth
    def ClickFeeMonth1(self):  # 选择调整费用相应的月份
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickFeeMonth1'.lower()].split('>')
        ClickFeeMonth1 = getElement(self.driver, locateType, locateExpression)
        return ClickFeeMonth1
    def ClickCurrAdjustmentBox(self):  # 当前调整费用Box
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickCurrAdjustment'.lower()].split('>')
        ClickCurrAdjustmentBox = getElement(self.driver, locateType, locateExpression)
        return ClickCurrAdjustmentBox
    def ClickCurrAdjustment1(self):  # 输入调整费用金额
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickCurrAdjustment1'.lower()].split('>')
        ClickCurrAdjustment1 = getElement(self.driver, locateType, locateExpression)
        return ClickCurrAdjustment1
    def ClickAddButton(self):  # 点击添加按钮
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickAddButton'.lower()].split('>')
        ClickAddButton = getElement(self.driver, locateType, locateExpression)
        return ClickAddButton
    def information(self):
        locateType, locateExpression = self.addAdustmentFee['Adustment.text'.lower()].split('>') #获取弹框上的message
        information = getElement(self.driver, locateType, locateExpression)
        return information.text
    def ClickConfirmBut(self):  # 点击弹框上面的确认
        locateType, locateExpression = self.addAdustmentFee['Adustment.ClickFinish'.lower()].split('>')
        ClickConfirmBut = getElement(self.driver, locateType, locateExpression)
        return ClickConfirmBut


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://gowins.imwork.net:7088/')
    login(driver, 'superadmin', 'superadmin')
    afa= AdustmentFeeAdd(driver)
    afa.financialManagement().click()
    afa.AdustmentFeeMangment().click()
    afa.AdustmentFeeMaintain().click()
    time.sleep(1)
    driver.switch_to.frame(afa.AdustmentFramList())
    time.sleep(4)
    afa.CliAdustmentAddBut().click()
    driver.switch_to.default_content()
    time.sleep(1)
    driver.switch_to.frame(afa.AdustmentAdcover())
    time.sleep(1)
    afa.MallBox().click()
    afa.ChooseMallData().click()
    time.sleep(1)
    afa.MerchantBox().click()
    afa.ChooseMerchantDate().send_keys('李宁')
    afa.ClikcMerSearBut().click()
    time.sleep(1)
    afa.MerchantResult().click()
    afa.ClickContractBox().click()
    afa.SearchContract().send_keys('XCSD181017001')
    afa.ClickContractSearBut().click()
    time.sleep(1)
    afa.ClickContractResult().click()
    time.sleep(1)
    afa.ClickSettGroupBox().click()
    afa.ChooseGroupInfo().click()
    time.sleep(1)
    afa.AccoutBox().click()
    afa.AccoutSearBox().click()
    afa.SearchAccount().send_keys('201804')
    afa.SearchAccountBut().click()
    afa.ClickAccountResu().click()
    time.sleep(1)
    afa.ClickAddFeeInfo().click()
    time.sleep(1)
    afa.ClickAddFeeBox().click()
    afa.ClickFeePBox1().click()
    time.sleep(2)
    afa.ClickFeeSear().send_keys('固定租金A')
    time.sleep(1)
    afa.ClickSFeeSearBut().click()
    afa.ClickSFeeResu().click()
    time.sleep(1)
    afa.FeeMonthBox().click()
    afa.ClickFeeMonth().click()
    afa.ClickFeeMonth1().click()
    time.sleep(1)
    afa.ClickCurrAdjustmentBox().click()
    time.sleep(1)
    afa.ClickCurrAdjustment1().clear()
    afa.ClickCurrAdjustment1().send_keys('300')
    afa.ClickAddButton().click()
    time.sleep(1)
    afa.ClickConfirmBut().click()









    


























