# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

class QichachaPipeline(object):

    def __init__(self):
        self.conn = psycopg2.connect(database="qichacha", user="dear", password="both-win", host="139.199.0.245",port="5432")
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        for i in item:
            item[i] = item[i].replace('\n','').replace('\t','').replace('\'','').replace('\"','').strip(' ')
        keys = ','.join(item.keys())
        values = '\',\''.join((item.values()))

        sql = "INSERT INTO company(%s) VALUES('%s')" % (keys,values)
        print sql
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print e
        return item

    def __del__(self):
        self.conn.close()
