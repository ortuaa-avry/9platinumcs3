# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](q1/classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|Title|string|Public|It is the most unique attribute of an object.|
|Director|string|Private|Not every viewer pays attention to the Director of a movie.
|Genre|string|Public|Viewers need to know what type of movie they are watching.|
|Year|int|Private|Not every viewer pays attention to when the movie was released.|
|Duration|float|Private|Not every viewer is concerned about how long the movie is.|
|Availability|boolean|Public|It tells whether the movie is available to watch or not.|
## Updated UML Class Diagram
![Class Diagram](Images/classDiagramSG5.png)
## Python Implementation
[View Python Source](classImplementation.py)
## Test Run
![Test Run](Images/classTestRun.png)
## Object Diagram
![Object Diagram](Images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
