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

    while True:
        city = input('\n Which city\'s data would you like to take a look at?').lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print('\n Sorry that wasn\'t an option. Please try again.')
            continue
        else:
            print('\n You selected: ', city)
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('\n Which month are you interested in seeing data from?').lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('\Invalid! There\'s no data associated with your input.')
            continue
        else:
            print('\n Your selected: ', month)
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('\n Now let\'s get your input for day of the week?').lower()
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('Please try again. Entry invalid!')
            continue
        else:
            print('\n You selected: ', day)
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

    df = pd.read_csv("chicago.csv")
    df = pd.read_csv("new_york_city.csv")
    df = pd.read_csv("washington.csv")

    # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])

    #extract month and day of week from Start Time to create new columns
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name

    #fitler by month if applicable
    if month != 'all':
        months=['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1

        #filter by month to create new dataframe
        df = df[df['month'] == month]

        #filter by day of week if applicable
        if day != 'all':
            #filter by day of week if applicable
            df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print ('\nThe most popular month to travel is:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nThe most popular day of the week is:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('\nThe most popular hour is:', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('\nThe most popular start station is:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('\nThe most popular end station is:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combo = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most common combination of start and end station trip is:', frequent_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time is:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\n These are the user types: ', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print('\n The Gender column does not exist')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(df['Birth Year'].min())
    else:
        print('\n This does not exist')

    if 'Birth Year' in df.columns:
        print(df['Birth Year'].max())
    else:
        print('\n Birth year does not exist')

    if 'Birth Year' in df.columns:
        print(df['Birth Year'].mode())
    else:
        print('\n The Birth year doesn\'t exist')

    print("\n This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    # Ask user if they'd like to see five additional lines of code
    index = 0

    while True:

        display_data = input('\n Would you like to see 5 additional lines of raw data? Yes or No?').lower()
        if display_data in ('yes', 'y'):
            print(df.iloc[index:index+5])
            index += 5
            continue
        else:
            if display_data in ('no', 'n'):
                print ('\n Thank you!')
        break

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
