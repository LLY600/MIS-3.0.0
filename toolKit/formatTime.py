import time
from datetime import timedelta, date

def dateTimeChineseFormat1():
	dateTime1 = time.strftime('%Yyear%mmonth%dday %Hhour%Mminute%Ssecond', time.localtime())
	dateTime2 = dateTime1.replace('year', '年').replace('month', '月').replace('day', '日').replace('hour', '时').replace('minute', '分').replace('second', '秒')
	return dateTime2
def dateTimeChineseFormat2():
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
def dateTimeChineseFormat3():
	return time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
def dateChineseFormat1():
	date1 = time.strftime('%Yyear%mmonth%dday', time.localtime())
	date2 = date1.replace('year', '年').replace('month', '月').replace('day', '日')
	return date2
def dateChineseFormat2():
	return time.strftime('%Y-%m-%d', time.localtime())
def dateChineseFormat3():
	return time.strftime('%Y/%m/%d', time.localtime())
def timeChineseFormat1():
	time1 = time.strftime('%Hhour%Mminute%Ssecond', time.localtime()).replace('hour', '时').replace('minute', '分').replace('second', '秒')
	return time1
def timeChineseFormat2():
	return time.strftime('%H:%M:%S', time.localtime())
def year():
	return time.strftime('%Y', time.localtime())
def month():
	return time.strftime('%m', time.localtime())
def day():
	return time.strftime('%d', time.localtime())
def hour():
	return time.strftime('%H', time.localtime())
def minute():
	return time.strftime('%M', time.localtime())
def seconds():
	return time.strftime('%S', time.localtime())
def strTime(sTime):
	return time.strptime(sTime, '%Y-%m-%d %H:%M:%S')
def addDate(dayNum):
	today = date.today()
	times = today + timedelta(days=dayNum)
	return times
def subDate(dayNum):
	today = date.today()
	times = today - timedelta(days=dayNum)
	return times
if __name__ == '__main__':
	print(dateTimeChineseFormat1())
	print(dateTimeChineseFormat2())
	print(dateTimeChineseFormat3())
	print(dateChineseFormat1())
	print(dateChineseFormat2())
	print(dateChineseFormat3())
	print(timeChineseFormat1())
	print(timeChineseFormat2())
	print(year())
	print(month())
	print(day())
	print(hour())
	print(minute())
	print(seconds())
	sTime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
	print(sTime)
	print(addDate(2))
	print(subDate(2))






















