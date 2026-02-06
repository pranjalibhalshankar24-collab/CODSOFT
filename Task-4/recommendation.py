movies = {
  "Avatar": "Sci-Fi",
    "Avengers": "Action",
    "Iron Man": "Action",
    "Inception": "Sci-Fi",
    "Gladiator": "Action",
    "The Matrix": "Sci-Fi",
    "Jurassic Park": "Adventure",
    "Jumanji": "Adventure",
    "Pirates of the Caribbean": "Fantasy",
    "Harry Potter": "Fantasy",    
}

user_preference = input("Enter movie genre (Action/Sci-Fi/Fantasy/Adventure): ")

recommended_movies = []

for movie, genre in movies.items():
    if genre.lower() == user_preference.lower():
        recommended_movies.append(movie)

if recommended_movies:
    print("Recommended Movies for you:")
    for movie in recommended_movies:
        print("-", movie)
else:
    print("No movies found for this genre.")