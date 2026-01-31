movies = {
    "Titanic": "Romance",
    "Avatar": "Sci-Fi",
    "Avengers": "Action",
    "Iron Man": "Action",
    "The Notebook": "Romance"
}

user_preference = input("Enter movie genre (Action/Romance/Sci-Fi): ")

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
