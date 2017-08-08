import json 
import os
<<<<<<< HEAD
import pprint
=======
>>>>>>> master

with open('scrap-pile/movienight/movies.json') as data_file:
    data = json.load(data_file)

#print(data)

#create url string "/movie-name/productionid"   

 for movie in data:
<<<<<<< HEAD

     mypath = (data[0]['title'].replace(" ", "-") + "/" + data[0]['productionid']).lower()  
     mypath  = str("https://www.regmovies.com/movies/" + mypath)
     
     print(mypath)

     
=======
     movie['title'].replace("", "-")
>>>>>>> master
