'''
添加区域场景用例
'''

from Action.login import *
from Action.addDistrict import *
from toolKit.readExcelFile import *
from toolKit.formatTime import *
from toolKit.screenCapture import *
from toolKit.compareFile import *

def test_add_district():
	driver = webdriver.Chrome()
	ref = ReadExcelFile(excelDataPath)
	ref.getSheetByName(u'登录地址账号')
	list1 = ref.getAllRows()[1:]
	for index01, row01 in enumerate(list1):
		if row01[4].value == 'Y':
			driver.get(str(row01[1].value))
			ref.writeValueToCell(dateTimeChineseFormat2(), index01 + 2, 6)
			loginId = row01[2].value
			password = row01[3].value
			try:
				assert login(driver, loginId, password) == '登录成功!', '登录失败！'
				ref.writeValueToCell('Pass', index01 + 2, 7)
				ref.getSheetByName(u'基础数据')
				sign = ref.get_start_sign(ref, u'添加区域')
				list2 = ref.cycle_index_list(ref, u'添加区域')
				for index02, row02 in enumerate(list2):
					if row02[4].value == 'Y':
						ref.writeValueToCell(dateTimeChineseFormat2(), index02 + sign + 2, 7)
						try:
							districtNum = row02[1].value
							districtName = row02[2].value
							districtEName = row02[3].value
							add_district_data(driver, districtNum, districtName, districtEName)
							adp = AddDistrictPage(driver)
							if adp.information() == row02[5].value:
								ref.writeValueToCell('Pass', index02 + sign + 2, 7)
							else:
								ref.writeValueToCell('Fail', index02 + sign + 2, 7)
								screenCapture(driver)
								assert False
						except:
							ref.writeValueToCell('Fail', index02 + sign + 2, 7)
							screenCapture(driver)
							assert False
						logger.info(u'<------以上是Excel表格第%s组测试数据------>' % str(index02 + 1))
						driver.refresh()
					else:
						ref.writeValueToCell('N/A', index02 + sign + 2, 7)
			except Exception as e:
				logger.info(u'异常信息：' + ''.join(e.args))
		else:
			ref.writeValueToCell('N/A', index01 + 2, 7)
			continue
	logger.info(u'***********该功能用例执行完毕!***********')
	driver.quit()
























