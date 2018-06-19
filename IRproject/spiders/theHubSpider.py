import scrapy

class theHubSpider(scrapy.Spider):
    name = "theHubSpider"

    
    start_urls = ["https://www.hub.lk/technology-design-forum/"]
       
    def parse(self, response):
        externalLinks = response.css("div.threadinfo div.inner h3.threadtitle a::attr(href)")
        for link in externalLinks:
            yield response.follow(link, self.parse_page)
        print ("==============================")

    
    def parse_page(self, response):
        print ("++++++++++++++++++++")
        title = response.xpath("/html/body/div[2]/div[5]/ol/li[1]/div[2]/div[2]/div[1]/h2/text()")
        auther = response.xpath("/html/body/div[2]/div[5]/ol/li[1]/div[2]/div[1]/div[2]/div/a/strong/text()")
        print (title)
        print (auther)
        print ("-----------------------")
