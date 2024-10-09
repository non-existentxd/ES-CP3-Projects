
class Movie:
    
    def __init__(self, title, year, director, rating, genre, cast):
        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast

    def __str__(self):
        return f"Title: {self.title}\nRelease year: {self.year}\nDirector: {self.director}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {self.cast}\n"

    def genre():
        genre = input("Which movie genre are you looking for?", (genre), "Write the type of Genre: ")
        if genre == Movie(genre):
            print("Here is a list of movies that go with that genre: ")
            print(Movie)
        else:
            return genre

    
    def director():
        director = input("Which movie director are you looking for?", (director), "Write their name: ")
        if director == Movie(director):
            print("Here is a list of movies the director has done: ")
            print(Movie)
        else:
            return director
       



    def cast():
        cast = input("Which movie actor are you looking for?", (cast), "Write their name:" )
        if cast == Movie(cast):
            print("Here is a list of movies these actors have playd in: ")
            print(Movie)
        else:
            return cast

m1= Movie("The Shaws Redemption", (1994), "Frank Darabont", "R", "Drama", "[Tim Robbins, Morgan Freeman]")
m2= Movie("Pulp Fiction", (1994), "Quentin Tarantino", "R", "Crime", "[John Travolta, Uma Thurman, Samuel L. Jackson]")
m3= Movie("The Godfather", (1972), "Francis Ford Coppola", "R", "Crime", "[Marlon Brando, Al Pacino, James Caan]")
m4= Movie("Inception", (2010), "Christopher Nolan", "PG-13", "Sci-Fi", "[Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page]")
m5= Movie("The Matrix", (1999), "Lana Wachowski", "Lilly Wachowski", "R", "Sci-Fi", "[Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss]")
m6= Movie("Forrest Gump", (1994), "Robert Zemeckis", "PG-13", "Drama", "[Tom Hanks, Robin Wright, Gary Sinise]")
m7= Movie("The Dark Knight", (2008), "Christopher Nolan", "PG-13", "Action", "[Christian Bale, Heath Ledger, Aaron Eckhart]")
m8= Movie("Schindler's List", (1993), "Steven Spielberg", "R", "Drama", "[Liam Neeson, Ben Kingsley, Ralph Fiennes]")
m9= Movie("Titanic", (1997), "James Cameron", "PG-13", "Romance", "[Leonardo DiCaprio, Kate Winslet, Billy Zane]")
m10= Movie("The Lord of the Rings: The Fellowship of the Ring", (2001), "Peter Jackson", "PG-13", "Fantasy", "[Elijah Wood, Ian McKellen, Orlando Bloom]")
m11= Movie("Jurassic Park", (1993), "Steven Spielberg", "PG-13", "Adventure", "[Sam Neill, Laura Dern, Jeff Goldblum]")
m12= Movie("The Lion King", (1994), "Roger Allers", "Rob Minkoff", "G", "Animation", "[Matthew Broderick, Jeremy Irons, James Earl Jones]")
m13= Movie("Eternal Sunshine of the Spotless Mind", (2004), "Michel Gondry", "R", "Romance", "[Jim Carrey, Kate Winslet, Kirsten Dunst]")
m14= Movie("The Sixth Sense", (1999), "M. Night Shyamalan", "PG-13", "Thriller", "[Bruce Willis, Haley Joel Osment, Toni Collette]")
m15= Movie("Braveheart", (1995), "Mel Gibson", "R", "Biography", "[Mel Gibson, Sophie Marceau, Patrick McGoohan]")
m16= Movie("The Terminator", (1984), "James Cameron", "R", "Sci-Fi", "[Arnold Schwarzenegger, Linda Hamilton, Michael Biehn]")
m17= Movie("Back to the Future", (1985), "Robert Zemeckis", "PG", "Adventure", "[Michael J. Fox, Christopher Lloyd, Lea Thompson]")
m18= Movie("Alien", (1979), "Ridley Scott", "R", "Horror", "[Sigourney Weaver, Tom Skerritt, John Hurt]")
m19= Movie("The Perks of Being a Wallflower", (2012), "Stephen Chbosky", "PG-13", "Drama", "[Logan Lerman, Emma Watson, Ezra Miller]")
m20= Movie("Dead Poets Society", (1989), "Peter Weir","PG", "Drama", "[Robin Williams, Robert Sean Leonard, Ethan Hawke]")

Movie()