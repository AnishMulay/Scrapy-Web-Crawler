import scrapy
from ..items import CrawlerItem

class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = [
		'https://quotes.toscrape.com/'
	]

	def parse(self, response):
		items = CrawlerItem()

		all_quotes = response.css('div.quote')
		
		for quote in all_quotes:
			title = quote.css('span.text::text').extract()
			author = quote.css('.author::text').extract()
			tags = quote.css('.tag::text').extract()
			
			items['title'] = title
			items['author'] = author
			items['tags'] = tags

			yield items