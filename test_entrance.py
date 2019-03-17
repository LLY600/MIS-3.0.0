# allure需环境及模块：pytest-allure-adaptor、allure、java
# 测试文件以test_开头（以_test结尾也可以）
# 测试类以Test开头，并且不能带有 __init__ 方法
# 测试函数以test_开头
# 使用命令行到此文件目录执行：py.test test_entrance.py --alluredir ./allureResult  生成测试数据保存allureResult路径下
# 使用命令行到此文件目录执行：allure generate ./allureResult/ -o ./allureReport/ --clean   在./allureReport/目录下就生成了Allure的测试报告
# –clean目的是先清空测试报告目录，再生成新的测试报告。
# 使用命令行到此文件目录执行：allure open -h 127.0.0.1 -p 8083 ./allureReport/    本机的浏览器将打开http://127.0.0.1:8083/index.html网页，展示测试报告

from Script.addProperty import *
from Script.addBusinessType import *
from Script.addGroup import *
from Script.addDistrict import *
from Script.addBuilding import *
from Script.addCell import *
from Script.confirmCell import *
from Script.addBrand import *
from Script.confirmBrand import *
from Script.addMerchant import *
from Script.confirmMerchant import *
from Script.addStore import *
from Script.addCommodityGroup import *
from Script.addSettlementGroup import *
from Script.addExpenseItem import *
from Script.addBackPaymentType import *
from Script.addBillAdjustType import *
from Script.marginCollection import *
from Script.marginCollectionConfirm import *
from Script.marginHandle import *
from Script.marginHandleConfirm import *
from Script.advancePaymentMaintenance import *
from Script.irregularCost import *
from Script.addAdustmentFee import *
from Script.billGeneration import *
from Script.billConfirm import *
from Script.billAdjust import *
from Script.billAdjustConfirm import *
from Script.addCollection import *
from Script.addCollectionConfirm import *
from Script.addLateFeeCollection import *
from Script.addLateFeeCollectionConfirm import *
# import allure
# import pytest


import unittest
import HTMLTestRunner

class RunAllCase(unittest.TestCase):
	# def test_case01(self):
	# 	test_add_property()  # 添加物业性质
	# def test_case02(self):
	# 	test_add_business_type()  # 添加业态信息
	# def test_case03(self):
	# 	test_add_group()  # 添加集团信息
	# def test_case04(self):
	# 	test_add_district()  # 添加区域信息
	# def test_case05(self):
	# 	test_add_building()  # 添加楼宇信息
	# def test_case06(self):
	# 	test_add_cell()  # 添加单元信息
	# def test_case07(self):
	# 	test_confirm_cell()  # 确认单元信息
	def test_case08(self):
		test_add_brand()  # 添加品牌信息
	# def test_case09(self):
	# 	test_confirm_brand()  # 确认品牌信息
	# def test_case10(self):
	# 	test_add_merchant()  # 添加商户信息
	# def test_case11(self):
	# 	test_confirm_merchant()  # 确认商户信息
	# def test_case12(self):
	# 	test_add_store()  # 添加店铺信息
	# def test_case13(self):
	# 	test_add_commodity_group()  # 添加货品组别
	# def test_case14(self):
	# 	test_add_settlement_group()  # 添加结算组别
	# def test_case15(self):
	# 	test_add_expense_item()  # 添加费用项目
	# def test_case16(self):
	# 	test_add_back_payment_type()  # 添加后台收款方式
	# def test_case17(self):
	# 	test_add_bill_adjust_type()  # 添加账单调整类型
	# def test_case18(self):
	# 	test_add_margin_collection()  # 添加保证金收取
	# def test_case19(self):
	# 	test_confirm_margin_collection()  # 确认保证金收取
	# def test_case20(self):
	# 	test_add_margin_handle()  # 添加保证金处理
	# def test_case21(self):
	# 	test_confirm_margin_handle()  # 确认保证金处理

	##################################################################
	# 如下3个用例由其他三位同学编写，未调试
	##################################################################
	# def test_case22(self):
	# 	irregularCost()  # 不规则费用
	# def test_case23(self):
	# 	advance()  # 预收款
	# def test_case24(self):
	# 	addAdustmentFee()  # 调整费用
	##################################################################

	# def test_case25(self):
	# 	test_add_bill_generation()  # 账单生成
	# def test_case26(self):
	# 	test_confirm_bill()  # 账单确认
	# def test_case27(self):
	# 	test_add_bill_adjust()  # 账单调整
	# def test_case28(self):
	# 	test_confirm_bill_adjust()  # 账单调整确认
	# def test_case29(self):
	# 	test_add_collection()  # 添加收款
	# def test_case30(self):
	# 	test_confirm_collection()  # 收款确认
	# def test_case31(self):
	# 	test_add_LateFee_collection()  # 滞纳金收款
	# def test_case32(self):
	# 	test_confirm_lateFee_collection()  # 滞纳金收款确认

if __name__ == '__main__':
	s = unittest.TestSuite()
	s.addTests(unittest.makeSuite(RunAllCase))
	filename = open('report.html', 'wb')
	runner = HTMLTestRunner.HTMLTestRunner(
		stream=filename,
		title='测试报告',
		description='详细报告内容'
	)
	runner.run(s)