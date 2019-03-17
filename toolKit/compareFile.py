import sys
from toolKit.log import *
import sys
from toolKit.log import *


def read_file(file):
	try:
		with open(file, 'r') as f:
			data = f.read()
			return data
			# list2 = f.read().splitlines()  # splitlines()：按照行('\r', '\r\n', \n')分隔，返回一个包含各行元素的列表
	except Exception as e:
		print(u'打开文件失败：', e)
		sys.exit(1)

def contain_file(actual_file,expect_file):  # 一个文件的内容包含于另一个文件中
	list1 = read_file(actual_file)
	list2 = read_file(expect_file)
	logger.info(u'开始与文件库进行对比')
	if list1 in list2:
		return '一致'
	else:
		return '不一致'

def match_file(actual_file,expect_file):
	logger.info(u'开始与文件库进行对比')  # 一个文件与另一个文件内容完全匹配
	list1 = read_file(actual_file)
	list2 = read_file(expect_file)
	if list1 == list2:
		return '一致'
	else:
		return '不一致'
