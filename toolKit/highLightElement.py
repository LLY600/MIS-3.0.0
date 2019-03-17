'''
高亮显示正在操作的元素
'''

from selenium import webdriver
import time

def highLightElement(driver, element):
	driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, "border:1.5px solid red;")
	time.sleep(1)

if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.get('https://www.baidu.com/')
	serchbox = driver.find_element_by_id('kw')
	highLightElement(driver, serchbox)
	serchbox.send_keys('python')