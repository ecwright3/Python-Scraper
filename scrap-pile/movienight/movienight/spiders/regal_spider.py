import scrapy
import json 



class movieDetailItem(scrapy.Item):
    #Theater Details
    title = scrapy.Field()
    productionid = scrapy.Field()
    rating = scrapy.Field()
    duration = scrapy.Field()
    screenformat = scrapy.Field()
    showtimes = scrapy.Field()
    theater = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    #Movie Details
    director = scrapy.Field()
    producer = scrapy.Field()
    writer = scrapy.Field()
    releasedate = scrapy.Field()
    runtime = scrapy.Field()
    synopsis = scrapy.Field()
    cast = scrapy.Field()

class RegalMovies (scrapy.Spider):
    name = "regal-movies"


    #start_urls = [
        #'https://www.regmovies.com/theaters/regal-westview-stadium-16-imax/8341',
        #'https://www.regmovies.com/theaters/regal-germantown-stadium-14/8459',
    #] 
    
    #Per https://doc.scrapy.org/en/latest/intro/tutorial.html
    def start_requests(self):
        urls = [
            'https://www.regmovies.com/theaters/regal-westview-stadium-16-imax/8341',
            'https://www.regmovies.com/theaters/regal-germantown-stadium-14/8459',
            ]
    
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
        
    def parse(self, response):
        

        for movie in response.css('ul.showtime-panel-list > li'):
            theater = response.css('div.page-header div.info-cell')
            data = movie.css('h3.title a::attr(data-csm)').extract_first()
            

            movieinfo = json.loads(data)

            #Handle theaters showing the same movie on multiple screens

            for screen in movie.css('div.showtime-panel > div.format-section'): 
                
                times = list(map(str.strip, screen.css('li.showtime-entry a::text').extract())) #remove the \n from showtimes list
                item = movieDetailItem()
                item['title'] = movieinfo['productionName']
                item['productionid'] = movieinfo['productionId']
                item['rating'] = movie.css('ul.list-inline title::text').extract_first()
                item['duration'] = movie.css('ul.list-inline li::text').extract()[2]
                item['screenformat'] = screen.css('div.format-section > a::attr(data-format-attribute-name)').extract_first()
                item['showtimes'] = times
                item['theater'] = theater.css('h1.title::text').extract_first()
                item['address'] = theater.css('div.address > a::text').extract_first()
                item['phone'] = theater.css('div.phone::text').extract_first().strip()


                movietitle = movie.css('h3.title a::attr(href)').extract_first()
                mypath = "https://www.regmovies.com/" + movietitle

                detailRequest = scrapy.Request(mypath, callback=self.parse_movieDetails)
                detailRequest.meta['movie_info'] = item

                yield detailRequest


    def parse_movieDetails(self, response):
        
        Info = response.css('div.dp-info-section')

        item = response.meta['movie_info']
        item['director'] =  Info.css('div.metadata > div::text').extract()[0] 
        item['producer'] = Info.css('div.metadata > div::text').extract()[1]
        item['writer'] = Info.css('div.metadata > div::text').extract()[2]
        item['releasedate'] = Info.css('div.metadata > div::text').extract()[3]
        item['runtime'] = Info.css('div.metadata > div::text').extract()[4]
        item['synopsis'] = Info.css('div.synopsis > div::text').extract_first()
        item['cast'] = Info.css('div.cast > ul > li::text').extract()
        
        yield item




    
