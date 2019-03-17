'''
封装获取元素的方法
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

def getElement(driver, locateType, locateExpression):
	try:
		element = WebDriverWait(driver, 8).until(lambda x: x.find_element(by=locateType, value=locateExpression))
		return element
	except Exception as e:
		raise e

def getElements(driver, locateType, locateExpression):
	try:
		elements = WebDriverWait(driver, 8).until(lambda x: x.find_element(by=locateType, value=locateExpression))
		return elements
	except Exception as e:
		raise e
if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get('https://www.baidu.com/')
	inputBox = getElement(driver, 'xpath', '//input[@id="kw"]')
	driver.quit()
