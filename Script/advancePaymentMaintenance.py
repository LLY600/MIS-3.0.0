# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException,NoSuchElementException
# import traceback
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://192.168.1.136:7088/')
# try:
#     wait = WebDriverWait(driver,10,0.2)  # 显示等待
#     loginId = wait.until(lambda x:x.find_element_by_xpath('//input[@id="username"]'))  # 用户名
#     loginId.send_keys('LLY01')
#     passWord = wait.until(lambda x:x.find_element_by_xpath('//*[@id="pwd"]'))  # 密码
#     passWord.send_keys('123456')
#     submit = wait.until(lambda x:x.find_element_by_xpath('//form[@id="login_form"]/p[3]/input'))  # 登录按钮
#     submit.click()
#
#
#
#     financialManagement = wait.until(lambda x:x.find_element_by_xpath('//*[@id="78"]/label'))  # 财务管理
#     financialManagement.click()
#     ysk = wait.until(lambda x: x.find_element_by_xpath('//*[@id="554"]/label'))  # 预收款管理
#     ysk.click()
#     yskwh = wait.until(lambda x: x.find_element_by_xpath('//*[@id="555"]/label'))  # 预收款维护  //*[@src="/manager/gw_advance_payment/gw_advance_payment_list.html?menuId=555&type=links"]
#     yskwh.click()
#     driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/manager/gw_advance_payment/gw_advance_payment_list.html?menuId=555&type=links"]'))  # 切换frame框架
#     time.sleep(3)
#     tjysk = wait.until(lambda x: x.find_element_by_xpath('//*[@id="addAdvancePayment()"]'))  # 添加预收款
#     tjysk.click()
#     driver.switch_to.default_content()  # 回到默认框架
#     time.sleep(3)
#     driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/manager/gw_settlement_payment/gw_settlement_payment_add.html?type=5"]'))
# #商户搜索
#     sh = driver.find_element_by_xpath('//*[@name="merchantCode_x"]') #商户空白框
#     sh.click()
#     sh_name = driver.find_element_by_xpath('//*[@name="cnName"]') #商户名称空白框
#     sh_name.send_keys('5S压榨')
#     ss = driver.find_element_by_xpath('//span[contains(text(), "搜索")]') #搜索按钮 增加行
#     ss.click()
#     time.sleep(1) #等待时间
#     result = driver.find_element_by_xpath('//*[@id="grid1007|1|r1001|c101"]/div')  #商户选择搜索结果
#     result.click()
# #合同搜索
#     contractName = driver.find_element_by_xpath('//input[@name="contractCode_x"]') # 合同号
#     contractName.click()
#     time.sleep(1)
#     contractNameSearchBox = driver.find_element_by_xpath('//input[@name="code"]') # 合同号搜索框 //*[@id="1539675432743_3_code"]
#     contractNameSearchBox.send_keys('XCSD180921006')
#     ss = driver.find_element_by_xpath('//*[@id="Form1028"]/div/ul/li[2]/div/span') #//*[@id="Form1029"]/div/ul/li[2]/div/span
#     ss.click()
#     time.sleep(1)
#     result = driver.find_element_by_xpath('//*[@id="grid1029|2|r1001|c102"]/div')
#     result.click()
#
# #添加收款
#     # skmxwbk = driver.find_element_by_xpath('//*[@id="depositPaymentDetail"]/div[1]/span')  #定位收款增加行 //*[@id="depositPaymentDetail"]/div[1]/span
#     # skmxwbk.click()
#     zjh = driver.find_element_by_xpath('//*[@id="depositPaymentDetail"]/div[3]/div/div[1]/span') #增加行
#     zjh.click()
#     skfs = driver.find_element_by_xpath('//*[@id="depositPaymentDetail|2|r1001|c101"]/div')# 收款方式 /html/body/div[1]/div[2]
#     skfs.click() #点击
#     time.sleep(1)
#     skfs.click()  # 点击
#     wxwz = driver.find_element_by_xpath('/html/body/div[10]/div[1]/table/tbody/tr[1]/td')
#     wxwz.click()
#
#     skje = driver.find_element_by_xpath('//*[@id="depositPaymentDetail|2|r1001|c102"]')#点击收款金额//*[@id="depositPaymentDetail|2|r1001|c102"]/div/div/div/input
#     skje.click()
#     # time.sleep(1)
#     # skje.click()  # 点击
#     sksrk = driver.find_element_by_xpath('//*[@id="depositPaymentDetail|2|r1001|c102"]/div/div/div/input')
#     time.sleep(0.5)
#     sksrk.clear()
#     sksrk.send_keys('1000')
#
# #保存
#     baoc = driver.find_element_by_xpath('/html/body/div[2]/a[1]') #确认
#     baoc.click()
#
#
#     tsdw = driver.find_element_by_xpath('//div[contains(text(), "是")]') # 是否添加
#     tsdw.click()
#
#     time.sleep(3)
#     driver.refresh()
#
#
#
# except:
#     pass
#
#
#######################################################################################################
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback

from Action.login import *
from Action.advancePayment import *
from toolKit.readExcelFile import *
from FilePath.readFilePath import *
from toolKit.log import *
from toolKit.formatTime import *
from toolKit.screenCapture import *
from PageObject.advancePaymentPage import *

def advance():
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
                ref.getSheetByName(u'添加预付款')
                rows_addMargin = ref.getAllRows()[1:]
                for index02, row02 in enumerate(rows_addMargin):
                    if row02[4].value == 'Y':
                        try:
                            merchantName = row02[1].value
                            contractName = row02[2].value
                            amount = str(row02[3].value)
                            logger.info(u'【第%s组测试数据】' % (index02 + 1))
                            advancePaymentModule(driver, merchantName, contractName,amount)
                            ap = AdvancePayment(driver)
                            if str(ap.information()) == str(row02[5].value):
                                ref.writeValueToCell('Pass', index02 + 2, 8)
                                logger.info(u'测试通过！')
                            else:
                                ref.writeValueToCell('Fail', index02 + 2, 8)
                                logger.info(u'测试失败！')
                                screenCapture(driver)  # 保存截图
                            ref.writeValueToCell(dateTimeChineseFormat2(), index02 + 2, 7)
                        except:
                            ref.writeValueToCell('Fail', index02 + 2, 8)
                            ref.writeValueToCell(dateTimeChineseFormat2(), index02 + 2, 7)
                            time.sleep(5)
                            screenCapture(driver)
                    else:
                         ref.writeValueToCell('N/A', index02 + 2, 8)
                         continue
                    time.sleep(2)
                    driver.refresh()
            except Exception as e:
                ref.getSheetByName(u'登录账号')
                ref.writeValueToCell('Fail', index01 + 2, 6)
                ref.writeValueToCell(dateTimeChineseFormat2(), index01 + 2, 5)
                logger.info(u'异常信息：' + ''.join(e.args))

            ref.getSheetByName(u'登录账号')
            ref.writeValueToCell('Pass', index01 + 2, 6)
            ref.writeValueToCell(dateTimeChineseFormat2(), index01 + 2, 5)

        else:
            ref.getSheetByName(u'登录账号')
            ref.writeValueToCell('N/A',index01 + 2,6)
            continue
    logger.info(u'---------------我是分割线---------------')
    driver.quit()








