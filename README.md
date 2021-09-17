## US Bikeshare Data Analysis Project
![Image of bikeshare](https://github.com/robertebong/pdsnd_github/blob/61241573a8b8dc35e5c5014b63018e0a49fedf37/bike-share-660.jpg)
[image from wttw](https://news.wttw.com/)
## Date created
17 September 2021

## Description
In this project, **Python** is used to explore data related to bike share systems for three major cities in the **United States of America :**  **Chicago**, **New York City**, and **Washington.**

The source code takes in raw input from the user to create an interactive experience.
Depending on the user's input, data is imported from source to provide answer to important question with the help of descriptive statistics.

## Software Requirements 
- You should have **Python 3, NumPy**, and **pandas** installed using **Anaconda**
- A text editor, like **Sublime or Atom**.
- A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

## Files used
- washington.csv
- new_york_city.csv
- chicago.csv
- bikeshare_2.py

## Project Details

### Bikeshare Data 

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, we use  data provided by  [Motivate](https://www.motivateco.com/) , a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. We can  compare the system usage between three large cities: **Chicago, New York City, and Washington, DC.**

### The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)
- The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year

### Statistics Computed
Users will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, users will write code to provide the following information:

##### 1 Popular times of travel (i.e., occurs most often in the start time)
- most common month
- most common day of week
- most common hour of day

##### 2 Popular stations and trip
- most common start station
- most common end station
- common trip from start to end (i.e., most frequent combination of start station and end station)

##### 3 Trip duration
- total travel time
- average travel time

##### 4 User info
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)


