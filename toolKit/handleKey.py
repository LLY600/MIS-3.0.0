import win32api
# import win32clipboard as w
import win32con
import time
from toolKit.log import *

#键盘按键映射字典
KB_CODE = {
	'enter': 0x0d,
	'ctrl': 0x11
}

def keyDown(keyName):  # 模拟键盘按下
	win32api.keybd_event(KB_CODE[keyName], 0, 0, 0)

def keyUp(keyName):  # 模拟键盘抬起
	win32api.keybd_event(KB_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

def handleAlert(cycleIndex,keyName):  # cycleIndex：循环点击次数
	try:
		for i in range(0, cycleIndex):
			time.sleep(1)
			keyDown(keyName)
			keyUp(keyName)
	except:
		logger.info(u'Alert未正常处理！')
