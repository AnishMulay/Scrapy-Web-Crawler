# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class CrawlerPipeline:
	def __init__(self):
		self.create_connection()
		self.create_table()

	def create_connection(self):
		self.con = sqlite3.connect("scrapedreviews.db")
		self.cur = self.con.cursor()

	def create_table(self):
		self.cur.execute("""drop table if exists reviews""")

		self.cur.execute("""create table reviews(
							id integer,
							body text
							)""")

	def store(self, item):
		self.cur.execute("""insert into reviews values (?)""",
		(
			item['body'][0],
		))
		self.con.commit()
	
	def process_item(self, item, spider):
		self.store(item)
		print("pipeline: " + item['body'][0])
		return item
