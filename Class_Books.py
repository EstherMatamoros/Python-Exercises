#Books

class Book:
    title = "Harry Potter and the Deathly Hallows"
    pages = 607
    number = "7th"
    genre = "fantasy"
    print(f"{title} has {pages} pages")
    print(f"It is the {number} in the series.")

#Movies

class Movie: 
    name = "Toy Story 3"
    start_time = "4:45pm"
    end_time = "6:32pm"

#instancia de la clases Movie usando el constructor Movie().Guardamos esta instancia en una variable llamada movie. 
movie = Movie()
print("Movie: " + movie.name)
print("Start: " + movie.start_time)
print("End: " + movie.end_time)