| Attribute | Data Type | Visibility | Why Public/Private? |
|---|---|---|---|
|Title|string|Public|It is the most unique attribute of an object.|
|Director|string|Private|Not every viewer pays attention to the Director of a movie.
|Genre|string|Public|Viewers need to know what type of movie they are watching.|
|Year|int|Private|Not every viewer pays attention to when the movie was released.|
|Duration|float|Private|Not every viewer is concerned about how long the movie is.|
|Availability|boolean|Public|It tells whether the movie is available to watch or not.|

+--------------------------------------------+
| Movie                                      |
+--------------------------------------------+
| + Title : string                           |
| + Genre : string                           |
| + Availability : boolean                   |
| - Director : string                        |
| - Year : int                               |
| - Duration : float                         |
+--------------------------------------------+
| + playback()                               |
| + present(title : string)                  |
| + release()                                |
+--------------------------------------------+

+--------------------------------------------+
| ClassName |
+--------------------------------------------+
| + publicAttribute : datatype |
| + publicAttribute : datatype |
| - privateAttribute : datatype |
| - privateAttribute : datatype |
+--------------------------------------------+
| + method() |
| + method(parameter : datatype)|
| + getSomething() |
+--------------------------------------------+
