import json
movies = open ("./movies.json",
encoding="utf8")
data = json.load(movies)

def get_movie(movies):
    for movie in movies:
            print(movie['name'], movie['release'])
get_movie(movies)