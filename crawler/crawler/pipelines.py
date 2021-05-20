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
		self.con = sqlite3.connect("scrapedquotes.db")
		self.cur = self.con.cursor()

	def create_table(self):
		self.cur.execute("""drop table if exists quotes""")

		self.cur.execute("""create table quotes(
							title text,
							author text,
							tag text
							)""")

	def store(self, item):
		self.cur.execute("""insert into quotes values (?, ?, ?)""",
		(
			item['title'][0],
			item['author'][0],
			item['tags'][0]
		))
		self.con.commit()
	
	def process_item(self, item, spider):
		self.store(item)
		print("pipeline: " + item['title'][0])
		return item
