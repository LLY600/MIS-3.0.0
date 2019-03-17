'''
读取配置文件数据
'''
from configparser import ConfigParser
from FilePath.readFilePath import *

class readConfigurationFile(object):
	def __init__(self):
		self.cf = ConfigParser()  # 生成解析器
		self.cf.read(pageObjectRepositoryPath, encoding='utf-8-sig')
	def getItemSection(self, sectionName):
		return dict(self.cf.items(sectionName))
	def getOptionValue(self, sectionName, optionName):
		return self.cf.get(sectionName, optionName)
if __name__ == '__main__':
	rcf = readConfigurationFile()
	print(rcf.getItemSection('addMarginCollection'))
	print(rcf.getOptionValue('addMarginCollection', 'addMarginCollection.addRow').split('>'))

