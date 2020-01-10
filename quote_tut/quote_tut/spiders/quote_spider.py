import scrapy 

class QuoteSpider(scrapy.Spider):
    name = 'quotes'


    start_url = 'http://quotes.toscrape.com/page/'

    index = [i for i in range(1,10)]
    start_urls = []
    for i in index:
        start_urls.append(start_url+str(i))



    def parse(self, response):
        all_quotes = response.css('div.quote')

        for quotes in all_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()
            yield {
                'title' : title,
                'author':author,
                'tags' : tags
            }

