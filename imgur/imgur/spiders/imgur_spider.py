import scrapy
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors import LinkExtractor
from imgur.items import ImgurItem

class ImgurSpider(CrawlSpider):
    


    name='imgur'
    allowed_domains=['http://imgur.com/']
    start_urls=['http://imgur.com/']
    rules=[Rule(LinkExtractor(allow=['/gallery/.*']),'parse_imgur')]
    
    def parse_imgur(self,response):
        
        image=ImgurItem()
        
        image['title']=response.xpath(\
            "//*[@id='u_0_1w']/div[2]/div[1]/div[5]/div/div/div/a").extract()
        rel=response.xpath("//*[@id='u_0_2c']").extract()
        image['image_urls']=['http:'+rel[0]]
        return image
            
            
        
            
	
