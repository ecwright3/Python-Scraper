import scrapy
import json 

class RegalMovies (scrapy.Spider):
    name = "regal-movies"


    start_urls = [
        'https://www.regmovies.com/theaters/regal-westview-stadium-16-imax/8341',
        'https://www.regmovies.com/theaters/regal-germantown-stadium-14/8459',
    ] 

    def parse(self, response):
        for movie in response.css('ul.showtime-panel-list > li'):
            theater = response.css('div.page-header > div.info-cell')
            #remove the \n from showtimes list 
            for screen in movie.css('div.showtime-panel > div.format-section'): 

                times = list(map(str.strip, screen.css('li.showtime-entry a::text').extract()))
                
                data = movie.css('h3.title a::attr(data-csm)').extract_first()
                movieinfo = json.loads(data)
                yield {
                    'title' : movieinfo['productionName'],
                    'productionid' : movieinfo['productionId'],
                    'rating' : movie.css('ul.list-inline title::text').extract_first(),
                    'duration' : movie.css('ul.list-inline li::text').extract()[2],
                    'format' : screen.css('div.format-section > a::attr(data-format-attribute-name)').extract_first(),
                    'showtimes': times,
                    'theater' : theater.css('h1.title::text').extract_first(),
                    'address' : theater.css('div.address > a::text').extract_first(),
                    'phone' : theater.css('div.phone::text').extract_first().strip(),
                }