class LibraryMaterial:
  def __init__(self, author, title):
    self.__author = author
    self.__title = title
  def author(self):
    print(f"Author: {self.__author}")
  def title(self):
    print(f"Title: {self.__title}")

class Book(LibraryMaterial):
  def __init__(self, number_pages):
    self.number_pages = number_pages
  def number_pages(self):
    self.number_pages
  def set_number_of_pages(number_pages):
    self.number_pages = 0
    
class Magazine(LibraryMaterial):
   def __init__(self, issue_number):
    self.issue_number = issue_number
  def issue_number(self):
    self.issue_number
  def set_issue_number(issue_number):
    self.number_pages = 0
