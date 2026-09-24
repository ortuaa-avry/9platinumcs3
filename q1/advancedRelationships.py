class Movie:
    def __init__(self, title, genre, availability, director, year, duration):
        # Public Attributes
        self.title = title
        self.genre = genre
        self.availability = availability

        # Private Attributes
        self.__director = director
        self.__year = year
        self.__duration = duration

    # Method 1
    def playback(self):
        print(f"Now Playing: {self.title} ({self.__year})")
        print(f"Directed by: {self.__director}")
        print(f"Duration: {self.__duration}hrs")

    # Method 2
    def present(self, new_title):
        self.title = new_title
        self.availability = True
        print(f"Movie is updated to: {self.title}")

    # Method 3
    def release(self):
        self.availability = True
        print(f"'{self.title}' is now available to watch!")


# Child class
class AnimatedMovie(Movie):
    def __init__(self, title, genre, availability, director, year, duration, animation_studio):
        super().__init__(title, genre, availability, director, year, duration)
        self.animation_studio = animation_studio

    def show_studio(self):
        print(f"Animation Studio: {self.animation_studio}")


class Watchlist:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Added '{movie.title}' to {self.name}.")

    def show_movies(self):
        print(f"\nWatchlist: {self.name}")
        print(f"Owner: {self.owner}")
        print("Movies in watchlist:")

        for movie in self.movies:
            print(f"- {movie.title}")
            print(f"  Genre: {movie.genre}")
            print(f"  Available: {movie.availability}")
# Movie objects
movie1 = Movie("Barbie in the Diamond Castle","Fantasy/Musical",True,"William Lau",2008,1.19)
movie2 = Movie("Barbie as the Princess and the Pauper","Musical/Fantasy",True,"William Lau",2004,1.25)
movie3 = Movie("Barbie: Fairytopia","Fantasy/Adventure",True,"Conrad Helten",2005,1.10)
# AnimatedMovie object demonstrating inheritance
animated1 = AnimatedMovie("Barbie and the Magic of Pegasus","Fantasy/Adventure",True,"Greg Richardson",2005,1.25,"Mainframe Entertainment")
# Watchlist object
watchlist1 = Watchlist("My Barbie Watchlist: Diamond Castle Collection","UserH2SO4")
# INHERITANCE TEST
print("===== INHERITANCE TEST =====")

print(f"Title: {animated1.title}")
print(f"Genre: {animated1.genre}")
print(f"Availability: {animated1.availability}")

animated1.playback()
animated1.show_studio()
# AGGREGATION TEST
print("\n===== AGGREGATION TEST =====")

watchlist1.add_movie(movie1)
watchlist1.add_movie(movie2)
watchlist1.add_movie(movie3)
watchlist1.add_movie(animated1)

watchlist1.show_movies()
# INDEPENDENT OBJECT TEST
print("\n===== INDEPENDENT OBJECT TEST =====")

movie1.release()
movie1.playback()

print("Movie 1 can still exist independently of the Watchlist.")
