import scrapy
import json 

class RegalSpider (scrapy.Spider):
    name = "regal-movies"


    start_urls = [
        #'https://www.regmovies.com/theaters/regal-westview-stadium-16-imax/8341',
        'https://www.regmovies.com/theaters/regal-germantown-stadium-14/8459'
    ] 

    def parse(self, response):
        for movie in response.css('ul.showtime-panel-list > li'):
            
            data = movie.css('h3.title a::attr(data-csm)').extract_first()
            movieinfo = json.loads(data) 
            yield {
                'title' : movieinfo['productionName'],
                'productionid' : movieinfo['productionId'],
                'rating' : movie.css('ul.list-inline title::text').extract_first(),
                'duration' : movie.css('ul.list-inline li::text').extract()[2],
                'showtimes' : movie.css('li.showtime-entry a::text').extract(), # The number of showtimes will change as the day passes. past show times will drop off.  
            }

        