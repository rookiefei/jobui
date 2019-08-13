# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Jobui1Pipeline(object):
    # 定义一个JobuiPipeline类，负责处理item
    def __init__(self):
        #连接MySql数据库
        self.connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='zf123456', db='jobui')
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        #往数据库中写入数据
        self.cursor.execute('insert into job_info(company,position,address,detail) values("{}","{}","{}","{}")'.format \
        (item['company'],item['position'],item['address'],item['detail']))
        self.connect.commit()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()