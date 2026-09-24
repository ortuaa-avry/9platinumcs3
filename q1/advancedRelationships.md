# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description: My existing system consists of two classes: Movie and Watchlist. The Movie class represents a movie and contains attributes such as title, genre, availability, director, year, and duration. It also has methods such as playback(), present(), and release(). The Watchlist class represents a collection of movies. It can contain zero or more Movie objects. For Part IV, I added an AnimatedMovie child class that inherits from the Movie class. I also changed the relationship between Watchlist and Movie from a general Association into Aggregation.
## Inheritance Relationship
Parent: Movie
Child: AnimatedMovie
Explanation: I chose Movie as the parent class and AnimatedMovie as the child class because an animated movie is a type of movie. The AnimatedMovie class inherits the common attributes and methods of the Movie class. It can use attributes such as title, genre, and availability, as well as methods such as playback(), present(), and release(). The AnimatedMovie class also has its own additional attribute called animation_studio and its own method called show_studio(). For my example, I used Barbie and the Diamond Castle as an AnimatedMovie object. This demonstrates how a specific animated movie can inherit the characteristics of the general Movie class.
## Inheritance UML
![Inheritance](Images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation
Explanation: The relationship between Watchlist and Movie is Aggregation because a Watchlist contains Movie objects, but the Movie objects can exist independently. In my program, the Movie objects are created separately before they are added to the Watchlist. The Watchlist only stores references to these existing Movie objects. This means that the Watchlist does not control the entire lifetime of the Movie objects. If the Watchlist is removed, the Movie objects can still exist independently.
## Advanced UML Diagram
![Advanced UML](Images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](Images/advancedTestRun.png)
## Object Diagram
![Objects](Images/advancedObjectDiagram.png)

## Reflection
Answers:
1. Explain why your child class is a type of your parent class. I chose Movie as the parent class and AnimatedMovie as the child class because an animated movie is a type of movie. Both classes share common characteristics such as title, genre, availability, director, year, and duration. The AnimatedMovie class can use the methods inherited from Movie while also having its own animation_studio attribute and show_studio() method. I used Barbie and the Diamond Castle as an example of an AnimatedMovie object.
2. Identify attributes or methods that were reused. Inheritance reduced duplicate code because I did not have to rewrite the common movie attributes and methods in the AnimatedMovie class. The child class reuses attributes such as title, genre, and availability from Movie. It also inherits methods such as playback(), present(), and release(). I used super().__init__() to reuse the constructor of the parent class instead of writing the same initialization code again.
3. Explain the lifecycle relationship between the two objects. My HAS-A relationship is Aggregation because the Watchlist contains Movie objects that can exist independently. The Movie objects are created separately before being added to the Watchlist. This means that the Watchlist does not control their entire lifetime. Even if the Watchlist is removed, the Movie objects can still exist independently. Therefore, Aggregation is appropriate for the relationship between Watchlist and Movie.
4. In Part III, I used Association to show that a Watchlist is connected to Movie objects. In Part IV, I represented this relationship more specifically as Aggregation because the Movie objects can exist independently from the Watchlist. I also added Inheritance between Movie and AnimatedMovie. This represents an IS-A relationship because an AnimatedMovie is a type of Movie.
5. My design follows the DRY principle because the common movie attributes and methods are written only once in the Movie class. The AnimatedMovie class inherits these features instead of repeating the same code. The child class only adds features that are specific to animated movies, such as animation_studio and show_studio().
