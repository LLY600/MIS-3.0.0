#################################################################################################################
# from selenium import webdriver                   #第一次书写的流水式脚本
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://192.168.1.136:7088/')
# time.sleep(1)
# loginId = driver.find_element_by_xpath('//*[@id="username"]')#用户名
# loginId.send_keys('LLY01')
# passWord = driver.find_element_by_xpath('//*[@id="pwd"]')#密码
# passWord.send_keys('123456')
# time.sleep(1)
# submit = driver.find_element_by_xpath('//*[@id="login_form"]/p[3]/input')
# submit.click()
# time.sleep(1)
# financialManagement = driver.find_element_by_xpath('//*[@id="78"]/label')#财务管理
# financialManagement.click()
# irregularCost = driver.find_element_by_xpath('//*[@id="229"]/label')#不规则费用
# irregularCost.click()
# irregularList =driver.find_element_by_xpath('//*[@id="1281"]/label')#不规则费用维护
# irregularList.click()
# driver.switch_to.frame(driver.find_element_by_xpath('//*[@src="/manager/gw_Irregular_charge/gw_irrgular_charge_list.html?menuId=1281&type=links"]'))#切换框架
# time.sleep(2)
# addIrregular = driver.find_element_by_xpath('//*[@id="addIrregularCost"]')#添加按钮
# addIrregular.click()
# driver.switch_to.default_content()#回到默认框架
# time.sleep(1)
# driver.switch_to.frame(driver.find_element_by_xpath('//*[@src="/manager/gw_Irregular_charge/gw_irrgular_charge_add.html"]'))#切换框架
# merchantName = driver.find_element_by_xpath('//input[@name="merchantCode_x"]')#商户名称
# merchantName.click()
# merchantNameSearchBox = driver.find_element_by_xpath('//*[@name="cnName"]') #商户名称搜索框
# merchantNameSearchBox.send_keys('5S压榨')
# merchantNameSearch = driver.find_element_by_xpath('//*[@id="Form1015"]/div/ul/li[2]/div/span') #商户名称搜索按钮
# merchantNameSearch.click()
# time.sleep(1)
# merchantNameSearchResult = driver.find_element_by_xpath('//td[@id="grid1016|1|r1001|c101"]/div') #选择第一个商户
# merchantNameSearchResult.click()
# time.sleep(1)
# contractName = driver.find_element_by_xpath('//input[@name="contractCode_x"]')#合同号
# contractName.click()
# contractNameSearchBox = driver.find_element_by_xpath('//input[@name="code"]')#合同号搜索框
# contractNameSearchBox.send_keys('XCSD180921001')
# contractNameSearch = driver.find_element_by_xpath('//*[@id="Form1025"]/div/ul/li[2]/div/span')#合同号搜索按钮
# contractNameSearch.click()
# time.sleep(1)
# contractNameSearchResult = driver.find_element_by_xpath('//td[@id="grid1026|1|r1001|c101"]/div') #选择第一个合同
# contractNameSearchResult.click()
# time.sleep(1)
# settlementGroup = driver.find_element_by_xpath('//input[@name="settlementGroupBm_x"]') #结算组别
# settlementGroup.click()
# settlementGroupChoose =driver.find_element_by_xpath('/html/body/div[6]/div[1]/table/tbody/tr/td/span') #选择第一个结算组别
# settlementGroupChoose.click()
# time.sleep(1)
# accountPayable =driver.find_element_by_xpath('//input[@name="realAccountPayable_x"]')#账期
# accountPayable.click()
# accountPayableSearchBox =driver.find_element_by_xpath('//input[@name="gridAccountPayable"]')#账期搜索框
# accountPayableSearchBox.send_keys('201902')
# accountPayableSearch =driver.find_element_by_xpath('//*[@id="Form1037"]/div/ul/li[2]/div/span')#账期搜索按钮（ID容易发生改变）
# accountPayableSearch.click()
# time.sleep(1)
# accountPayableChoose =driver.find_element_by_xpath('//*[@id="grid1038|1|r1001|c101"]/div') #选择第一个账期（ID容易发生改变）
# accountPayableChoose.click()
# time.sleep(2)
# addCost =driver.find_element_by_xpath('//*[@id="gwIrregularGrid"]/div[3]/div/div[1]/span')#增加费用信息
# addCost.click()
# time.sleep(1)
# costName =driver.find_element_by_xpath('//td[@id="gwIrregularGrid|2|r1001|c101"]')#费用项目
# costName.click()
# costName.click()
# costNameSearchBox =driver.find_element_by_xpath('//input[@name="name"]')#费用名称
# time.sleep(1)
# costNameSearchBox.send_keys('不规则费用')
# time.sleep(1)
# # accountPayableSearch =driver.find_element_by_xpath('//span[text()="搜索")]')#费用名称搜索按钮//*[@id="Form1052"]/div/ul/li[2]/div/span
# # accountPayableSearch =driver.find_element_by_xpath('//div[@class="btn"]/following-sibling::div[7]/div/ul/li[2]/div/span')#费用名称搜索按钮//*[@id="Form1052"]/div/ul/li[2]/div/span
# # js = "document.getElementByClassName('l-button').click()"
# # driver.execute_script(js)
# accountPayableSearch = driver.find_element_by_xpath('//*[@id="Form1052" or @id="Form1062" or @id="Form1072"]/div/ul/li[2]/div/span')  #费用名称搜索按钮
# accountPayableSearch.click()
# time.sleep(1)
# accountPayableChoose =driver.find_element_by_xpath('//td[@id="grid1053|1|r1001|c101"]/div') #选择第一个费用名称
# accountPayableChoose.click()
# time.sleep(1)
# costMoney =driver.find_element_by_xpath('//*[@id="gwIrregularGrid|2|r1001|c102"]')#费用金额
# costMoney.click()
# costMoney2 =driver.find_element_by_xpath('//*[@id="gwIrregularGrid|2|r1001|c102"]/div/div/div/input')#再次点击费用金额，清除文本数据
# costMoney2.click()
# costMoney2.clear()
# costMoney2.send_keys('1200.00')
# time.sleep(1)
# costMonth =driver.find_element_by_xpath('//*[@id="gwIrregularGrid|2|r1001|c103"]')#费用月份//*[@id="gwIrregularGrid|2|r1001|c102"]/div/div/div/input
# costMonth.click()
# costMonth2 = driver.find_element_by_xpath('//*[@id="gwIrregularGrid|2|r1001|c103"]/div/div/div/div/input')
# costMonth2.click()
# costMonthChoose =driver.find_element_by_xpath('/html/body/div[8]/div[1]/table/tbody/tr[1]/td/span')#选择第一个月份
# costMonthChoose.click()
# time.sleep(1)
# note = driver.find_element_by_xpath('//td[@id="gwIrregularGrid|2|r1001|c104"]')#备注
# note.click()
# note2 = driver.find_element_by_xpath('//*[@id="gwIrregularGrid|2|r1001|c104"]/div/div/div/input')#备注
# note2.send_keys('备注信息')
# time.sleep(1)
# addButton = driver.find_element_by_xpath('/html/body/div[2]/a[1]')#添加
# addButton.click()
# time.sleep(1)
# driver.refresh()

#######################################################################################################################
'''
不规则费用(封装添加不规则费用，从Excel中读取数据)
'''
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback

from Action.login import *
from toolKit.readExcelFile import *
from FilePath.readFilePath import *
from toolKit.log import *
from toolKit.formatTime import *
from Action.addIrregularCost import *
from toolKit.screenCapture import *


def irregularCost():
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
                time.sleep(2)
                ref.getSheetByName(u'添加不规则费用')
                ref.addIrregular = ref.getAllRows()[1:]
                for index02, row02 in enumerate(ref.addIrregular):
                    if row02[7].value =='Y':
                        try:
                            merchantName = row02[1].value
                            contractId = row02[2].value
                            accountPayable = row02[3].value
                            costName = row02[4].value
                            money = row02[5].value
                            note = row02[6].value
                            logger.info(u'【第%s组测试数据】' % (index02 + 1))
                            addIrregularCostModule(driver, merchantName, contractId, accountPayable, costName, money, note)
                            aic = AddIrregularCostPage(driver)
                            if aic.information() == row02[8].value:
                                ref.writeValueToCell('Pass', index02 + 2, 11)
                                logger.info(u'测试通过！')
                            else:
                                ref.writeValueToCell('Fail', index02 + 2, 11)
                                logger.info(u'测试失败！')
                                screenCapture(driver)
                                assert False
                        except:
                            ref.writeValueToCell('Fail', index02 + 2, 11)
                            ref.writeValueToCell(dateTimeChineseFormat2(), index02 + 2, 10)
                            screenCapture(driver)  # 保存截图
                            assert False
                        ref.writeValueToCell(dateTimeChineseFormat2(), index02 + 2, 10)  # 221
                    else:
                        ref.writeValueToCell('N/A', index02 + 2, 11)
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
            ref.writeValueToCell('N/A', index01 + 2, 6)
            continue
    logger.info(u'---------------我是分割线---------------')
    driver.quit()
