import scrapy

class theHubSpider(scrapy.Spider):
    name = "theHubSpider"

    
    start_urls = ["https://www.hub.lk/technology-design-forum/"]
       
    def parse(self, response):
        externalLinks = response.css("div.threadinfo div.inner h3.threadtitle a::attr(href)")
        for link in externalLinks:
            yield response.follow(link, self.parse_page)
    
    def parse_page(self, response):
        title = response.xpath("/html/body/div[2]/div[5]/ol/li[1]/div[2]/div[2]/div[1]/h2/text()")
        author = response.xpath("/html/body/div[2]/div[5]/ol/li[1]/div[2]/div[1]/div[2]/div/a/strong/text()")
        startedDate = response.xpath("/html/body/div[2]/div[5]/ol/li[1]/div[1]/span[1]/span/text()")
        startedTime = response.xpath("/html/body/div[2]/div[5]/ol/li[1]/div[1]/span[1]/span/span/text()")
        description = response.xpath("/html/body/div[2]/div[5]/ol/li[1]/div[2]/div[2]/div[1]/div/div/blockquote/text()")
        category = response.xpath("/html/body/div[2]/div[1]/ul/li[4]/a/span/text()")
        print (title.extract_first(), author.extract(), startedDate.extract(),startedTime.extract(), description.extract(), category.extract())


        