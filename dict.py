movies = [{'name': "Pokemon: The First Movie",
            'release': 1999,
            'characters': ["Ash", "Pikachu", "Brock", "Misty", "Ambertwo", "Doctor Fuji", "Meowth", "James", "Jessie"],
            'genres': ["Sci-fi", "Adventure", "Fantasy"],
            },
            
            {'name': "Mewtwo Strikes Back",
            'release': 2019,
            'characters': ["Ash", "Pikachu", "Brock", "Misty", "Mewtwo", "Meowth", "James", "Jessie"],
            'genres': ["Sci-fi", "Fantasy", "Adventure"],
            },

            {'name': "Pokémon the Movie: The Power of Us",
            'release': 2018,
            'characters': ["Ash", "Brock", "Misty", "James", "Jessie", "Meowth", "Risa", "Pikachu", "Zeraora"],
            'genres': ["Sci-fi", "Fantasy", "Adventure"],
            }]
def get_movie(movies):
    for movie in movies:
        if 'Fantasy' in movie['genres']:
            print(movie['name'], movie['release'])
get_movie(movies)