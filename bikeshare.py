import time
import pandas as pd
import numpy as np

# loading files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
selected_cities = ['chicago', 'new york', 'washington']
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """       
    print('Hello! I am Marwa!! Let\'s explore some US bikeshare data!')
    print('-:-'*30)
    
    # To get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs to handling the unexpected input by user
    city = input('Do you want to look for data for Chicago, New York, or Washington? ').lower()
    while city not in selected_cities:
        print('You entered invalid city name not in the list')
        city = input('Do you want to look for data for Chicago, New York, or Washington? ').lower()
    
    # To get user input for filter type (month, day or both).
    filter = input('Would you like to filter the data by month, day, both, or none? ').lower()
    while filter not in(['month', 'day', 'both', 'none']):
        print('You entered invalid filter not in the list')
        filter = input('Do you want to filter the data by month, day, both, or none? ').lower()
    
        # To get user input for month ( January, February, March, April, May, June, or all)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if filter == 'month' or filter == 'both':
        month = input('Which month - January, February, March, April, May, or June? ').lower()
        while month not in months:
            print('You entered invalid month not in the list')
            month = input('Which month whould you like to select - January, February, March, April, May, or June? ').lower()
    else:
        month = 'all'
        
    # To get user input for day of week (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if filter == 'day' or filter == 'both':
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
        while day not in days:
            print('You entered invalid day not in the list')
            day = input('Which day whould you like to select: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
    else:
        day = 'all'
    
    print('-:-'*30)
    return city, month, day

def load_data(city, month, day):
    
    # Loads data for the specified city
    print('\nDATA is loading now.. .. .. ..\n')
    df = pd.read_csv(CITY_DATA[city])
    
    # To convert the Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # To extract month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
        
    # Filter by month 
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[ df['month'] == month ]

    # Filter by day of week
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    '''
    What is the most popular hour of day for start time?
    What is the most popular day of week for start time?
    What is the most popular month for start time?
    '''

    # To displays the statistics of the most frequent times of travel
    print('\nWhat is the most frequent times of travel?....\n')
    print('\nCalculating the most frequent times of travel...\n')
    start_time = time.time()
    
    # To display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)
    
    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)
    
    # To display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-:-'*30)
    
def station_stats(df):
    # To displays statistics on the most popular stations and trip

    print('\nWhat is the most popular stations and trip...\n')
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # To display the most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f'The most popular start station is: { most_common_start_station}')

    # To display the most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f'The most popular end station is: {most_common_end_station}')

    # To display the most frequent combination of start station and end station trip
    most_common_start_end_station = df['Start Station'] + ' to ' + df['End Station']
    print(f'The most popular trip is: from {most_common_start_end_station.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-:-'*30)   
    
def trip_duration_stats(df):
    from datetime import timedelta as td
    # To displays statistics on the total and average trip duration

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # To display the total travel time
    total_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days =  total_travel_duration.days
    hours = total_travel_duration.seconds // (60*60)
    minutes = total_travel_duration.seconds % (60*60) // 60
    seconds = total_travel_duration.seconds % (60*60) % 60
    print(f'The total travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds')

    # To display the average travel time
    average_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days =  average_travel_duration.days
    hours = average_travel_duration.seconds // (60*60)
    minutes = average_travel_duration.seconds % (60*60) // 60
    seconds = average_travel_duration.seconds % (60*60) % 60
    print(f'The average travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-:-'*20)
    
def user_info(df):
    # To displays statistics on bikeshare users

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # To display counts of user types
    print(df['User Type'].value_counts())
    print('\n\n')

    # To display counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())
        print('\n\n')

    # To display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns):
        year = df['Birth Year'].fillna(0).astype('int64')
        print(f'Earliest birth year is: {year.min()}\nmost recent is: {year.max()}\nand most comon birth year is: {year.mode()[0]}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-:-'*30)

def display_raw_data(df):
    
    # To displays the data used to compute the stats
    raw = input('\nDo you want to diplay raw data?\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count = count + 5
            ask = input("\nDo you want to see five more rows of the data used to compute the stats? Please enter 'yes' or 'no'? \n")
            if ask.lower() != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_info(df)
        display_raw_data(df)

        restart = input('\nDo you want to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
