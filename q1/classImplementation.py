class Movie:
  def __init__(self, title, genre, availability, director, year, duration):
  #Public Attributes
    self.title = value1
    self.genre = value2
    self.availability = availability
  #Private Attributes
    self.__director = director
    self.__year = year
    self.__duration = duration
#Method 1
  def playback(self):
    print(f"Now Playing: {self.title} ({self.__year})")
    print(f"Directed by: {self.__director}, Duration: {self.__duration}hrs")
#Method 2
  def present(self, new_title):
    self.title = new_title
    self.availability = True
    print(f"Movie title is updated to: {self.title}")
#Method 3
  def release(self):
    self.availability = True
    print(f"'{self.title}' is now available to watch!")

#Object 1 I LOVE MAMMA MIAAAA
movie1 = Movie("Mamma Mia!", "Musical/Comedy", False, "Phyllida Llyod", 2008, 1.48)
#Object 2 MERYL STREEP DA GOAT
movie2 = Movie("The Devil Wears Prada", "Comedy/Drama", True, "David Frankel", 2006, 1.49)

#Status before object 1 was changed
print("BEFORE:")
print(f"Movie 1: {movie1.title}, Available: {movie1.availability}")
print(f"Movie 2: {movie2.title}, Available: {movie2.availability}\n")

#Method on Object 1 only
movie1.playback()
print()

#Final Status
print("AFTER:")
print(f"Movie 1: {movie1.title}, Available: {movie1.availability}")
print(f"Movie 2: {movie2.title}, Available: {movie2.availability}")
