'''
封装异常截屏功能
'''
from FilePath.readFilePath import *
import time
from toolKit.log import *


def screenCapture(driver):
	screenPath = screenCapturePath  # 指定保存目录
	screenName = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()) + '.png'  # 截图命名
	wholePath = screenPath + screenName
	try:
		time.sleep(2)
		logger.info(u'测试失败，正在截屏，保存位置：%s' % wholePath)
		result = driver.get_screenshot_as_file(wholePath)
		return result
	except Exception as e:
		logger.info(u'异常信息：' + ''.join(e.args))

