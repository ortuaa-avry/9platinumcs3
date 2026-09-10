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
#Movies kez
movie1 = Movie("Mamma Mia!","Musical/Comedy",False,"Phyllida Lloyd",2008,1.48)
movie2 = Movie("The Devil Wears Prada","Comedy/Drama",True,"David Frankel",2006,1.49)
movie3 = Movie("Mary Poppins Returns","Musical/Fantasy",True,"Rob Marshall",2018,2.10)

#Watchlist
watchlist1 = Watchlist("My Watchlist: Movies I love, I like", "UserH2SO4")

# BEFORE RELATIONSHIP
print("--- BEFORE RELATIONSHIP ---")
print(f"Movie 1: {movie1.title}")
print(f"Movie 2: {movie2.title}")
print(f"Movie 3: {movie3.title}")
print(f"Watchlist: {watchlist1.name}")
print(f"Number of movies in watchlist: {len(watchlist1.movies)}")

# BUILDING RELATIONSHIP
print("\n--- BUILDING RELATIONSHIP ---")

watchlist1.add_movie(movie1)
watchlist1.add_movie(movie2)
watchlist1.add_movie(movie3)

# AFTER RELATIONSHIP
print("\n--- AFTER RELATIONSHIP ---")
watchlist1.show_movies()

# ACCESS DATA THROUGH RELATIONSHIP
print("\n--- ACCESSING MOVIE DATA THROUGH WATCHLIST ---")
for movie in watchlist1.movies:
    movie.playback()
    print()
