import logging
import logging.config
from FilePath.readFilePath import *

logging.config.fileConfig(logPath)  # 读取日志文件
logger = logging.getLogger('example02')  # 选择一个日志格式

def debug(message):
	logger.debug(message)
def info(message):
	logger.info(message)
def warning(message):
	logger.warning(message)
def error(message):
	logger.error(message)
def critical(message):
	logger.critical(message)

if __name__ == '__main__':
	error('bug!')
	info('hello word')
	warning('bad girl')
