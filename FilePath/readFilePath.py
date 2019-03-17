'''
封装存储文件的路径
'''

import os
projectPath = os.path.dirname(os.path.dirname(__file__))  # 项目的绝对路径
pageObjectRepositoryPath = projectPath + u'/Configure/pageObjectRepository.ini'  # 页面对象库文件的绝对路径
excelDataPath = projectPath + u'/TestData/测试数据表.xlsx'  # Excel数据表路径
logPath = projectPath + u'/Configure/logger.conf'
reportPath = projectPath + u'/Report/testReport.html'
screenCapturePath = projectPath + u'/TestData/ScreenCaptures//'
listData = projectPath + u'/TestData/ListData//'
fileLibrary = projectPath + u'/TestData/FileLibrary//'
compareResultPath = projectPath + u'/Report/compareResult.html'
tempTest = projectPath + u'/File/test.log'


if __name__ == '__main__':
	print('项目路径：', projectPath)
	print('页面对象仓库路径：', pageObjectRepositoryPath)
	print('Excel数据表路径：', excelDataPath)
	print('日志配置文件路径：', logPath)
	print('测试报告文件路径：', reportPath)
	print('屏幕截屏文件路径：', screenCapturePath)
	print(tempTest)
	print(listData)
	print(fileLibrary)
	print(os.path.exists(projectPath))
	print(os.path.exists(pageObjectRepositoryPath))
