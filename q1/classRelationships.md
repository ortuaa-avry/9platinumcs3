# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Movie
Description: A movie is a series of visual images shown rapidly in succession to create the illusion of a moving picture, typically telling a story or sharing an idea with sound.
## New Related Class
Class: Song
Description: A song is a short piece of music that includes words, vocals, and melody.
## Association
Relationship: Has-A
Explanation: Most movies have songs because they enhance the emotions that are being portrayed on a specific scene.
## Multiplicity

Multiplicity: 0..*
Explanation: Both classes can have multiple similarities.
## UML Class Relationship Diagram
![Class Relationship Diagram](Images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](Images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](Images/objectRelationshipDiagram.png)
## Analysis
### My two classes have a title, genre, and their availabilities can be determined.
### I chose 0..* because my classes can have multiple similar attributes.
### I implemented a relationship in python by connecting two classes through their similar attributes.
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
