import scrapy 

class QuoteSpider(scrapy.Spider):
    name = 'quotes'


    start_url = 'http://quotes.toscrape.com/page/'

    index = [i for i in range(1,10)]
    start_urls = []
    for i in index:
        start_urls.append(start_url+str(i))
    

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/',
    #         # 'http://quotes.toscrape.com/page/2/',
    #         ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.css('title::text').extract()


        yield {'title':title}
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

