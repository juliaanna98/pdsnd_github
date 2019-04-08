import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input('Would you like to see data for Chicago, New York or Washington?').lower()
    while not(city == "chicago" or city == "new york" or city == "washington"):
        print("City isn't valid... choose from Washington, Chicago or New York")
        city=input('Would you like to see data for Chicago, New York or Washington?').lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('Would you like to filter data by month? January, February, March, April, May or June?').lower().title()
    while not(month=='January' or month=='February' or month=='March' or month=='April' or month=='May' or month=='June'):
        print("Month isn't valid...chosose from January, February, March, April,May or June ")
        month=input('Would you like to filter data by month? January, February, March, April, May or June?').lower().title()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?').lower().title()
    while not(day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday" or day=="Saturday" or day=="Sunday"):
        print('Not valid')
        day=input('Which day? Mon, Tue, Wed, Thur, Fri, Sat or Sun?').lower().title()
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        df = df[df['day_of_week'] == day]
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)
 
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('Most Commonly Used Start Sation:', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('Most Commonly Used End Sation:', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_combination= df['Station Combination'] = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    
    print('Most Popular Combination: ', popular_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user=df['User Type'].value_counts()
    print (count_user)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender=df['Gender'].value_counts()
        print (count_gender)
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Gender' in df.columns:
        earliest_birth=df['Birth Year'].min()
        recent_birth=df['Birth Year'].max()
        popular_birth=df['Birth Year'].mode()[0]
        print("Oldest subscriber was born in: ", earliest_birth)
        print("Most recent birth: ", recent_birth)
        print("Most populat birth year: ",popular_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    display=input("Would you like to see first five lines of raw data? yes/no?")
    while display=='yes':
        print(df.head())
        display_more=input("Would you like to see five more?")
        n=5
        if display_more=='yes':
            n+=5
            print(df.head(n))
        else:
            break
            
        
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
