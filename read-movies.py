import json 
import os

with open('scrap-pile/movienight/movies.json') as data_file:
    data = json.load(data_file)

#print(data)

#create url string "/movie-name/productionid"   

 for movie in data:
     movie['title'].replace("", "-")