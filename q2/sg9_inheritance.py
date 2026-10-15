class Publication:
  def __init__(self, author, title):
    self.__author = author
    self.__title = title
  def display_info(self):
    print(f"Author: {self.__author}")
    print(f"Title: {self.__title}")

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = None
        self.number_of_pages = number_of_pages

    @property
    def number_of_pages(self):
        return self.__number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, value):
        if value <= 0:
            print("The number of pages must be positive.")
        else:
            self.__number_of_pages = value

    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.number_of_pages)

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.issue_number = issue_number

    @property
    def issue_number(self):
        return self.__issue_number

    @issue_number.setter
    def issue_number(self, value):
        if value <= 0:
            print("The issue number must be positive.")
        else:
            self.__issue_number = value

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.issue_number)

publication1 = Publication("Introduction to Science", "John Smith")
publication2 = Publication("World History", "Mary Santos")

book1 = Book("The Picture of Dorian Gray", "Oscar Wilde", 254)
book2 = Book("The Metamorphosis", "Franz Kafka", 70)

magazine1 = Magazine("National Geographic", "Susan Goldberg", 1)
magazine2 = Magazine("TIME", "Sam Jacobs", 25)

print("=== PUBLICATIONS ===")
publication1.display_info()
print()
publication2.display_info()

print("\n=== BOOKS ===")
book1.display_info()
print()
book2.display_info()

print("\n=== MAGAZINES ===")
magazine1.display_info()
print()
magazine2.display_info()
