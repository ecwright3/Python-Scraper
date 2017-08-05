
## Required Components

I'm still working on what I want to do. 
I want to come up with a project that would be helpful to Cyber Security Teams. 

For nowthis will just be uses ad my scratch pad until I come up with a good idea. 

Making a left turn now going to scrap Movie sites to start building a date night app.

Target Site: https://www.regmovies.com/theaters/regal-westview-stadium-16-imax/8341

response.css('ul.showtime-panel-list li')   

movie = response.css('ul.showtime-panel-list li')[0] 

movie.css('h3.title a::attr(data-csm)').extract_first()  # Gives movie title and movie id
 
movie.css('ul.list-inline title::text').extract_first() # Movie Rating
 
movie.css('ul.list-inline li::text').extract()[2] # Movie Duration 

movie.css('li.showtime-entry a::text').extract() # Movie Showtimes 
