import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('Would you like to see data for Washington, New York, or Chicago?').lower()
    while city not in (CITY_DATA.keys()):
        print('You provided invalid city name')
        city = input('Would you like to see data for Washington, New York, or Chicago?').lower()


# get user filter types (all, january, february, ... , june)

    filt = input('Would you like to filter the data by month, day , both, or none ? ').lower()
    while filt not in (['month','day','both','none']):
        print('You provided invalid filter')
        filt = input('Would you like to filter the data by month, day , both, or none ?').lower()

# get user input for month (all, january, february, ... , june)

    months = ['january','february','march','april','may','june']

    if filt == 'month' or filt == 'both':
        month = input('Which month - January, February, March, April, May, or June?').lower()
        while month not in months:
            print('you provided an invalid  month')
            month = input('Which month - January, February, March, April, May, or June ?').lower()

    else:
        month = 'all'

# get user input for day of week (all, monday, tuesday, ... sunday)

    days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    if filt == 'day' or filt == 'both':
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?').title()
        while day not in days:
            print('you provided an invalid  day')
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?').title()

    else:
        day = 'all'




    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading data file into  dataframe
    df = pd.read_csv(CITY_DATA[city])


    #converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract the day of the week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable 
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month =months.index(month) + 1

        #filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of the week if applicable
    if day != 'all':

        #filter by day to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january','february','march','april','may','june']
    month = df['month'].mode()[0]
    print(f'The most common month is :{months[month-1]}')

    # display the most common day of week
    day = df['day_of_week'].mode()[0]
    print(f'The most common day of week is :{day}')


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    prevalent_hour = df['hour'].mode()[0]
    print(f'the most common start hour is :{prevalent_hour}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    prevalent_start_station = df['Start Station'].mode()[0]
    print(f'The most popular start station is:{prevalent_start_station}')

    # display most commonly used end station
    prevalent_end_station = df['End Station'].mode()[0]

    print(f'The most popular end station is:{prevalent_end_station}')


    # display most frequent combination of start station and end station trip
    prevalent_trip = df['Start Station'] + ' ' '<<<<to>>>>' ' '  + df['End Station']
    print(f'The most popular trip is from : {prevalent_trip.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    start_time = time.time()
    # display total travel time
    travel_duration = df['Trip Duration'].sum()
    hours = travel_duration // (60*60)
    minutes = travel_duration % (60*60) // 60 
    seconds = travel_duration % (60*60) % 60
    print(f'Total travel time is : {hours}hours {minutes} minutes {seconds} seconds') 



    # display total travel time
    average_duration = df['Trip Duration'].mean()
    hours = average_duration // (60*60)
    minutes = average_duration % (60*60) // 60
    seconds = average_duration % (60*60) % 60
    print(f'Average travel time is :  {hours}hours {minutes} minutes {seconds} seconds') 

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())
    print('\n\n')


    # Display counts of gender
    if 'Gender' in (df.columns):
        print(df['Gender'].value_counts())
        print('\n\n')
    else:
        print("There is no gender information in this city.")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in (df.columns):
        x = df['Birth Year'].mean()
        year = df['Birth Year'].fillna(x,inplace = False).astype('int64')
        print (f'The Earliest birth year is:{year.min()} \nThe most recent  birth year is: {year.max()} \nAnd the most common year of birth is:{year.mode()[0]}')

    else:
        print("There is no birth year information in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Display raw data in 5 rows 

def display_raw_data(df):

    """Ask user if he wants to display the raw data and print 5 rows at a time"""
    pd.set_option('display.max_columns',50)
    raw_data = input('\nWould you like to display raw data? Enter yes or no?\n ')
    if raw_data.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Display  Next >>> 5 rows  ? Enter yes or no?')
            if ask.lower() != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
