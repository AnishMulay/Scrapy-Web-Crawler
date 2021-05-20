import scrapy
import re
from ..items import ReviewItem

class QuoteSpider(scrapy.Spider):
	name = 'reviews'
	# start_urls = [
	# 	'https://quotes.toscrape.com/'
	# ]
	start_urls = [
		'https://www.rottentomatoes.com/m/superman_man_of_steel/reviews'
	]

	def clean(str):
		cleanr = re.compile('<.*?>')
		cleantext = re.sub(cleanr, '', str)
		whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
		cleantext = ''.join(filter(whitelist.__contains__, cleantext))
		cleantext = re.sub(' +', ' ', cleantext)
		return cleantext

	def parse(self, response):
		# items = CrawlerItem()
		# all_quotes = response.css('div.quote')
		
		# for quote in all_quotes:
		# 	title = quote.css('span.text::text').extract()
		# 	author = quote.css('.author::text').extract()
		# 	tags = quote.css('.tag::text').extract()	
		# 	items['title'] = title
		# 	items['author'] = author
		# 	items['tags'] = tags
		# 	yield items

		# #if the website has a next link for pages that can be followed
		# next_page = response.css('li.next a::attr(href)').get()
		# if next_page is not None:
		# 	yield response.follow(next_page, callback=self.parse)

		# #if there is pagination in the website, this can be used to overcome that
		# next_page = 'https://quotes.toscrape.com/page/'+str(QuoteSpider.page_number)+'/'
		# if QuoteSpider.page_number < 11:
		# 	QuoteSpider.page_number += 1
		# 	yield response.follow(next_page, callback=self.parse)

		items = ReviewItem()

		all_reviews = response.css('.the_review').extract()
		count = 1

		for review in all_reviews:
			review = QuoteSpider.clean(review)
			items['id'] = count
			items['body'] = review
			count += 1
			yield items