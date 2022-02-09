import scrapy


class ProductSpider(scrapy.Spider):
    name = 'products'
    # allowed_domains = ['x']
    start_urls = ['https://techinstr.myshopify.com/collections/all']

    def parse(self, response):
        for link in response.xpath('//*[@id="Collection"]/div/div[1]/div/a@href').get():
            yield response.follow(link, callback=self.parse_product)


    def parse_product(self, response):
        img_link = [] # Creating an empty list

        # running loop in img_src link to get img
        for img in response.xpath("//*[@id='gs6999835967546']/@src").getall():
            img_link.append(response.urljoin(img)) # appending received img_src with img_link






