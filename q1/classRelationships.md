# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Movie
Description: A movie is a series of visual images shown rapidly in succession to create the illusion of a moving picture, typically telling a story or sharing an idea with sound.
## New Related Class
Class: Watchlist
Description: A Watchlist represents a collection of movies that a user wants to watch. It has its own name and owner, and it can contain multiple Movie objects.
## Association
Relationship: Has-A
Explanation: A watchlist needs actual movies to make up its collection.
## Multiplicity

Multiplicity: 0..*
Explanation: This means one Watchlist can contain zero or more Movie objects. A watchlist can initially be empty, and movies can be added later. This multiplicity also fits the requirement to practice using a Python list to store multiple object references.
## UML Class Relationship Diagram
![Class Relationship Diagram](Images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](Images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](Images/objectRelationshipDiagram.png)
## Analysis
### The association between my two classes is that a Watchlist contains Movie objects. The Watchlist is used to keep track of movies that a user wants to watch. In my system, watchlist1 contains movie1, movie2, and movie3. This connects the Watchlist object to the individual Movie objects.
### I chose a 1 : 0..* multiplicity between Watchlist and Movie. This means that one Watchlist can contain zero or more Movie objects. This is appropriate because a watchlist can be empty when it is first created and can have many movies added to it later. It also allows my program to demonstrate a one-to-many relationship.
### I implemented the relationship by creating a movies list inside the Watchlist class. The list is initialized with self.movies = []. I created an add_movie() method that adds an actual Movie object to the list using self.movies.append(movie). This allows the Watchlist to keep references to multiple Movie objects.
### I stored an object reference because the relationship should connect the actual objects instead of duplicating their information. For example, when I use watchlist1.add_movie(movie1), the actual movie1 object is stored inside the Watchlist's movies list. Because of this, the Watchlist can access movie1's attributes and methods, such as movie.playback().
### A list is appropriate because one Watchlist can contain many Movie objects. The movies list stores the actual references to movie1, movie2, and movie3. I can use a loop to go through each Movie object in the list. This makes it easy to manage and display all the movies in the Watchlist.
