class Movie:
    def __init__(self, title, year, director, rating, genre, cast):
        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast

    def __str__(self):
        return f"Title: {self.title}\nRelease Year: {self.year}\nDirector: {self.director}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {', '.join(self.cast)}\n"


    def sortTitle(movies):
        return sorted(movies, key=lambda movie: movie.title)

    def sortYear(movies):
        return sorted(movies, key=lambda movie: movie.year)


    def genre1(movies, genre):
        return [movie for movie in movies if genre.lower() in movie.genre.lower()]


    def director1(movies, director):
        return [movie for movie in movies if director.lower() in movie.director.lower()]


    def cast1(movies, actor):
        return [movie for movie in movies if any(actor.lower() in cast_member.lower() for cast_member in movie.cast)]





movies = [
    Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"]),
    Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]),
    Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"]),
    Movie("Inception", (2010), "Christopher Nolan", "PG-13", "Sci-Fi", "[Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page]"),
    Movie("The Matrix", (1999), "Lana Wachowski", "R", "Sci-Fi", "[Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss]"),
    Movie("Forrest Gump", (1994), "Robert Zemeckis", "PG-13", "Drama", "[Tom Hanks, Robin Wright, Gary Sinise]"),
    Movie("The Dark Knight", (2008), "Christopher Nolan", "PG-13", "Action", "[Christian Bale, Heath Ledger, Aaron Eckhart]"),
    Movie("Schindler's List", (1993), "Steven Spielberg", "R", "Drama", "[Liam Neeson, Ben Kingsley, Ralph Fiennes]"),
    Movie("Titanic", (1997), "James Cameron", "PG-13", "Romance", "[Leonardo DiCaprio, Kate Winslet, Billy Zane]"),
    Movie("The Lord of the Rings: The Fellowship of the Ring", (2001), "Peter Jackson", "PG-13", "Fantasy", "[Elijah Wood, Ian McKellen, Orlando Bloom]"),
    Movie("Jurassic Park", (1993), "Steven Spielberg", "PG-13", "Adventure", "[Sam Neill, Laura Dern, Jeff Goldblum]"),
    Movie("The Lion King", (1994), "Rob Minkoff", "G", "Animation", "[Matthew Broderick, Jeremy Irons, James Earl Jones]"),
    Movie("Eternal Sunshine of the Spotless Mind", (2004), "Michel Gondry", "R", "Romance", "[Jim Carrey, Kate Winslet, Kirsten Dunst]"),
    Movie("The Sixth Sense", (1999), "M. Night Shyamalan", "PG-13", "Thriller", "[Bruce Willis, Haley Joel Osment, Toni Collette]"),
    Movie("Braveheart", (1995), "Mel Gibson", "R", "Biography", "[Mel Gibson, Sophie Marceau, Patrick McGoohan]"),
    Movie("The Terminator", (1984), "James Cameron", "R", "Sci-Fi", "[Arnold Schwarzenegger, Linda Hamilton, Michael Biehn]"),
    Movie("Back to the Future", (1985), "Robert Zemeckis", "PG", "Adventure", "[Michael J. Fox, Christopher Lloyd, Lea Thompson]"),
    Movie("Alien", (1979), "Ridley Scott", "R", "Horror", "[Sigourney Weaver, Tom Skerritt, John Hurt]"),
    Movie("The Perks of Being a Wallflower", (2012), "Stephen Chbosky", "PG-13", "Drama", "[Logan Lerman, Emma Watson, Ezra Miller]"),
    Movie("Dead Poets Society", (1989), "Peter Weir","PG", "Drama", "[Robin Williams, Robert Sean Leonard, Ethan Hawke]")
]

def search_movies():
    search_type = input("Search by Genre (g), Director (d), or Cast (c)? [g/d/c]: ").lower()

    if search_type == 'g':
        genre = input("Enter the genre: ")
        result = Movie.genre1(movies, genre)
    elif search_type == 'd':
        director = input("Enter the director's name: ")
        result = Movie.director1(movies, director)
    elif search_type == 'c':
        actor = input("Enter the actor's name: ")
        result = Movie.cast1(movies, actor)
    else:
        print("Invalid option. Try again.")
        return search_movies()

    if result:
        for movie in result:
            print(movie)
    else:
        print("No movies found.")
    return search_movies()


def start():
    question = input("Hello! We have 20 movies. Would you like them all sorted by alphabet or by year? [a/y]: ")
    if question == 'a':
        sorted_movies = Movie.sortTitle(movies)
    elif question == 'y':
        sorted_movies = Movie.sortYear(movies)
    else:
        return start()

    for movie in sorted_movies:
        print(movie)
        
    question2 = input("Would you like to search for a specific movie by genre, director, or cast? [y/n]: ").lower()

    if question2 == 'y':
        search_movies()
    else:
        print("Thanks for browsing our movie list!")


start()
