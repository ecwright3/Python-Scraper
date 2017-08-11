import scrapy
import json 
from movienight.items import MovienightTheaterItem


#Get List of theaters and their address from regal



class RegalTheaters(scrapy.Spider):
    name = "regal-theaters"

    start_urls = [
        "https://www.regmovies.com/theater-list"
    ]

    def parse(self, response):
        theaters = response.css('ul.grid > li')
        theater_link = theaters.css('li > ul.list-unstyled a::attr(href)').extract()

        for link in theater_link:
            url = "https://www.regmovies.com" + link
            yield scrapy.Request(url=url, callback=self.parseTheaterInfo, dont_filter=True)


    def parseTheaterInfo(self, response):
        
        location = response.css('div.outer-map-container')

        item = MovienightTheaterItem()

        item['theaterName'] = location.css('h1.title::text').extract_first()
        item['theaterOneLineAddress'] = location.css('div.address a::text').extract_first()
        item['theaterPhone'] = location.css('div.phone::text').extract_first().strip()
        item['theaterCode'] = response.url.split('/')[-1]
        item['theaterUrl'] = response.url
        item['theaterSelfCoordinates'] = location.css('div.address a::attr(href)').extract_first().split('/')[-1].strip('@')

        CensusUrl = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=" + item['theaterOneLineAddress'] + "&benchmark=9&format=json"

        CensusRequest = scrapy.Request(CensusUrl, callback=self.parse_TheaterDetails, dont_filter=True)
        CensusRequest.meta['theater_Info'] = item

        yield CensusRequest

    def parse_TheaterDetails(self, response):

        result = response.css('body p::text').extract_first()
        locate = json.loads(result)

        item= response.meta['theater_Info']
        item['theaterState'] = locate['result']['addressMatches'][0]['addressComponents']['state']
        item['theaterCity'] = locate['result']['addressMatches'][0]['addressComponents']['city']
        item['theaterZip'] = locate['result']['addressMatches'][0]['addressComponents']['zip']
        item['theaterGovCoordinates'] = locate['result']['addressMatches'][0]['coordinates']

        yield item


