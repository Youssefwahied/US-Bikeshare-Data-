import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    
    while True:
        Cities = ['Chicago', 'New York', 'Washington']
        city = input('Would you like to see data for Chicago, New York, or Washington? \n> ').title()
        if city in Cities:
            break
        
    # get user input for month (all, january, february, ... , june)

    while True:
        Months = ['January', 'February', 'March', 'April', 'May', 'June','All']
        month = input('Which month - January, February, March, April, May, or June? if no filter needed choose all \n> ').title()
        if month in Months:
                 break
        
    
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','All']
        day = input(' Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? if no filter needed choose all \n> ').title()
        if day in Days:
                break
   
                   
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'All':
        Months = ['January', 'February', 'March', 'April', 'May', 'June','All']
        month = Months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'All':   
        df = df[df['day'] == day.title()]
    return df
                    
                         
def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month= df['month'].mode()[0]
    print("The most common month is :", most_common_month)
    
    # display the most common day of week
    most_common_day= df['day'].mode()[0]
    print("The most common day is :", most_common_day)
   
    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common hour is :", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is :",  most_commonly_used_start_station)

    # display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is :",  most_commonly_used_end_station)
    
    
    # display most frequent combination of start station and end station trip
    df['Combination'] = df ['Start Station'] + ' and ' + df ['End Station']
    most_frequent_combination_of_start_station_and_end_station_trip = df['Combination'].mode()[0]
    print("The most frequent combination of start station and end station trip is :",  most_frequent_combination_of_start_station_and_end_station_trip)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time is:",  total_travel_time)
    

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean travel time is:",  mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df["User Type"].value_counts()
    print("Counts of user types are: \n>",  counts_of_user_types)

    # Display counts of gender
    if 'Gender' in df.columns:

        counts_of_gender = df["Gender"].value_counts()
    
        print("Counts of user gender are: \n>",  counts_of_gender)
    else :
        print ("No gender information found")
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        
        earliest_year_of_birth = df["Birth Year"].min()
        print("The earliest year of birth is :",  earliest_year_of_birth)

        most_recent_year_of_birth = df["Birth Year"].max()
        print("Most recent year of birth is :",  most_recent_year_of_birth)

        most_common_year_of_birth = df["Birth Year"].mode()[0]
        print("Most common year of birth is :",  most_common_year_of_birth)
    else :
        print ("No birth year information found")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data) == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Would you like to continue with the next 5 rows ? Enter yes or no\n'").lower()
        continue 
        
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
