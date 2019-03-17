'''
封装从数据库读取数据功能
'''

# import cx_Oracle
import pymysql
from prettytable import PrettyTable
from FilePath.readFilePath import *
from toolKit.log import *



class Mysql(object):
	def __init__(self):
		self.address = '192.168.1.136'
		self.user = 'root'
		self.password = 'root'
		self.dataBase = 'gdws_mis_g_3.0'
	def marginCollectionList(self):  # 保证金收取列表数据
		sql = u'SELECT  b.name, (CASE a.status WHEN 1 THEN "新增(待确认)" WHEN  2  THEN "确认通过"  ' \
		      'WHEN 3 THEN "取消确认" END) AS statusType, (CASE a.type  WHEN 4 THEN "保证金"  ' \
		      'WHEN 7 THEN "预付款转保证金" END) AS type, a.contract_code,  a.merchant_name, d.name, a.payment_money, ' \
		      'a.payment_time FROM gw_payment_main AS a INNER JOIN gw_mall_info AS b ON a.mall_id = b.id INNER JOIN ' \
		      'gw_admin_users AS c ON a.mall_id = c.mall_id  INNER JOIN gw_shops_lease AS d ON a.shop_code = d.code  WHERE  a.type=4 ' \
		      'OR a.type=7  GROUP BY payment_code ORDER BY payment_code DESC LIMIT 1'
		fileName = listData + 'marginCollectionList.log'
		connect = pymysql.connect(self.address, self.user, self.password, self.dataBase, use_unicode=True, charset="utf8")  # 连接数据库
		cursor = connect.cursor()  # 使用corsor()方法创建一个游标对象
		cursor.execute(sql)  # 使用execute()方法执行SQL查询
		marginCollectionData = cursor.fetchall()  # 使用fetchall()方法获取所有数据
		logger.info(u'连接数据库，获取列表数据')
		table = PrettyTable(
			['购物中心', '状态', '类别', '合同号', '经营商户', '经营店铺', '收款金额', '收款时间'])
		table.align['购物中心'] = '1'
		table.padding_width = 1
		for row in marginCollectionData:
			table.add_row(list(row))
		cursor.close()
		connect.close()
		print(table)
		with open(fileName, 'w') as file:
			file.write(str(table))
		logger.info(u'将获取数据写入文件，保存位置:%s' % fileName)
if __name__ == '__main__':
	mysql = Mysql()
	mysql.marginCollectionList()
