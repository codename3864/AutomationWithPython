# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class QuoteTutPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect('quotes.db')
        self.curr = self.conn.cursor()


    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""CREATE table quotes_tb(
            title text,
            author text,
            tags text
            )""")


    def process_item(self, item, spider):
        self.store_db(item)
        print('title-----:'+item['title'][0])
        return item


    def store_db(self,item):
        self.curr.execute("""INSERT into quotes_tb values(?,?,?)""",(
            item['title'][0],
            item['author'][0],
            item['tags'][0]
            ))
        self.curr.execute("SELECT *FROM quotes_tb")
        print(self.curr.fetchall())
        self.conn.commit()

