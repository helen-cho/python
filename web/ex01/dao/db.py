import pymysql
import json

file = open('./dao/config.json', 'r', encoding='utf-8')
config = json.loads(file.read())

connection = pymysql.connect(
 host=config['host'],
 user=config['user'],
 password=config['password'],
 db=config['db'], 
 charset='utf8',
 cursorclass=pymysql.cursors.DictCursor)