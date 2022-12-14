import time
import pandas as pd
import numpy as np

df = pd.read_csv("chicago.csv")

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
CITIES = list(CITY_DATA.keys())

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = None
    month = None
    day = None
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        CITIES = list(CITY_DATA.keys())
        city = input('Choose a city: chicago, new york city, washington: ').lower()
        if city not in CITIES:
            print('Wrong choice, try again! ')
            continue
        else:
            break
          

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month = input('Choose a month: January, February, March, April, May, June or All: ').lower()
        if month not in MONTHS:
            print('Wrong choice, try again! ')
            continue
        else: 
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
        day = input('Choose a day of the week or all: ').lower()
        if day not in DAYS: 
            print('Wrong answer, try again! ')
            continue
        else:
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

    df = pd.read_csv(CITY_DATA[city])

           
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTHS.index(month) +1
        df = df[df['month'] == month]
        
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        df = df[df['day_of_week'] == day.title()]
  
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()
    
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)
    
    common_day = df['day_of_week'].mode()[0]
    print('Most common day: ', common_day)
    
    df['hour'] = df['Start Time'].dt.hour
    
    common_hour = df['hour'].mode()[0]
    print('Most common hour: ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    
    

   
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    import time
    start_time = time.time()
    
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('Popular Start Station: ', popular_start_station)
    
    common_station = df['End Station'].value_counts().idxmax()
    print('Common Used End Station: ', common_station)
    
    combination_stations = df.groupby(['Start Station', 'End Station']).count()
    print('Frequent Combination of Start Station and End Station trip: ', popular_start_station, common_station)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_trip_duration = df['Trip Duration'].sum()
    print('Total travel time: ', total_trip_duration)
    
       
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time)
              


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

 
def user_stats(df, city_name):
    """Displays statistics on bikeshare users.

    """
    
    print('\nCalculating User Stats...\n')
    
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Please see here user types: " + str(user_types))

    # TO DO: Display counts of gender

    
    if city_name == 'chicago.csv' or city_name == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("Please see here gender types: " + str(gender))
        
   
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('The most earliest year is: {}\n'.format(earliest_birth))
        print('The most recent year is: {}\n'.format(most_recent_birth))
        print('The most common year is: {}\n'.format(most_common_birth) )

   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def view_data(df):
    i = 0
    while True:
        rows = input('Do you want to see more data? yes/no: ')
        if rows.lower() == ('yes'):
            print(df[i:i+5])
            i = i+5
        else:
            break
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()