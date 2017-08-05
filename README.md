# Save-Soundcloud

Implement Spotify's Web API to extract and manipulate data. Through this project, the goal is to learn how API's work and how to build applications around user functionality and data visualization.


## Contributors

- Ash
- Julian Marks
- Richa Wadaskar


## Idea #1: Get your Playlist Poppin

[In a 2001 study done by University of Washington,](https://www.youtube.com/watch?v=b6dT4kyVUuY) researchers found a correlation between art and sex. They theorized that much of the books, movies, and music all follow a pattern of build up, climax, and resolution much like in sex. This bell curve like structure is found to be the most appealing and satifyings expereinces for us to consume. So why shouldn't our playlist follow this? 
![alt text](https://i2.wp.com/studentry.sg/wp-content/uploads/2013/08/bell-curve.jpg "Optimal Drunk Level")

The idea behind this project is to rearrange a user's playlist into a bell curve using the bpm of the songs (also other information if possible).  

### Learn about API's 

In order to get started on this project we are going to have to know what an API is and how it works. Here's some things I found along the way: 

[A pretty simple introduction into API's.](https://gigaom.com/2010/10/29/using-apis-not-quite-as-hard-as-it-looks/)

[Some more reading into API's.](http://technologyadvice.com/blog/information-technology/how-to-use-an-api/)

After having a grasp on API's and their functionality, we would need to know how to implement them. This is possible in many different languages. [Python](https://spotipy.readthedocs.io/en/latest/) has it's own Spotipy wrapper that supposedly does a lot of the work for us. 

Whatever lanuage we decide to do, we will inevitably be dealing with Spotify's own [Web API](https://developer.spotify.com/web-api/). There, we can sign up for an authentication key and understand all the different endpoints Spotify provides for us. Going through the documentation will give us a better stance of what is possible and hopefully serve inspiration for the scope of the project. 

### The Script's Functionality

Taking input for the username and playlist title, we would use that information to extract data about the playlist. We would then make a [dataframe](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) of the song titles and bpm's and use [numpy's normal function](https://stackoverflow.com/questions/20011494/plot-normal-distribution-with-matplotlib) to have a data frame of our new playlist. We would then use the API and create a new playlist in the order of our new dataframe. 

### Other Possibilities with the API
Here's a list of Data Science projects that implement Spotify's Web API:

[R Project](http://rcharlie.com/2017-02-16-fitteR-happieR/) 

[Another R Project](https://www.r-bloggers.com/my-new-r-package/)

[NYC Data Academy's Project](http://blog.nycdatascience.com/student-works/explorify-visualize-playlists/)


# Updates

## 27 July 2017

- First gained authentication through access code

### Goals

- Learn more about API navigation
	- What are important endpoints and their attributes?


## 3 Aug 2017

- Experimented with requests to the Spotify API
	- How to implement access code
	- Access to album, artist, and track endpoints

### Goals

- requirements.txt
- Project Structure and Design
- Setup Virtual environment