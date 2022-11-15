
```python
import pandas as pd
```


```python
import numpy as np
```


```python
df = pd.read_csv("chicago.csv")
```


```python
df.shape
```




    (300000, 9)




```python
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
CITIES = list(CITY_DATA.keys())
```


```python
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


```


```python
city, month, day = get_filters()
```

    Hello! Let's explore some US bikeshare data!
    Choose a city: chicago, new york city, washington: chicago
    Choose a month: January, February, March, April, May, June or All: may
    Choose a day of the week or all: monday
    ----------------------------------------



```python
def load_data(city, month, day):
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




    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df
```


```python
df =  load_data(city, month, day)
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Start Time</th>
      <th>End Time</th>
      <th>Trip Duration</th>
      <th>Start Station</th>
      <th>End Station</th>
      <th>User Type</th>
      <th>Gender</th>
      <th>Birth Year</th>
      <th>month</th>
      <th>day_of_week</th>
      <th>hour</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>43</th>
      <td>915409</td>
      <td>2017-05-22 05:49:43</td>
      <td>2017-05-22 05:51:15</td>
      <td>92</td>
      <td>Clark St &amp; Congress Pkwy</td>
      <td>LaSalle St &amp; Jackson Blvd</td>
      <td>Subscriber</td>
      <td>Male</td>
      <td>1967.0</td>
      <td>5</td>
      <td>Monday</td>
      <td>5</td>
    </tr>
    <tr>
      <th>54</th>
      <td>702079</td>
      <td>2017-05-01 08:35:17</td>
      <td>2017-05-01 08:49:02</td>
      <td>825</td>
      <td>Sedgwick St &amp; North Ave</td>
      <td>Michigan Ave &amp; Oak St</td>
      <td>Subscriber</td>
      <td>Male</td>
      <td>1983.0</td>
      <td>5</td>
      <td>Monday</td>
      <td>8</td>
    </tr>
    <tr>
      <th>89</th>
      <td>763995</td>
      <td>2017-05-08 17:29:05</td>
      <td>2017-05-08 17:39:32</td>
      <td>627</td>
      <td>Franklin St &amp; Jackson Blvd</td>
      <td>Franklin St &amp; Chicago Ave</td>
      <td>Subscriber</td>
      <td>Male</td>
      <td>1975.0</td>
      <td>5</td>
      <td>Monday</td>
      <td>17</td>
    </tr>
    <tr>
      <th>92</th>
      <td>760491</td>
      <td>2017-05-08 12:00:14</td>
      <td>2017-05-08 12:07:23</td>
      <td>429</td>
      <td>Clark St &amp; Lake St</td>
      <td>Dearborn St &amp; Erie St</td>
      <td>Subscriber</td>
      <td>Male</td>
      <td>1963.0</td>
      <td>5</td>
      <td>Monday</td>
      <td>12</td>
    </tr>
    <tr>
      <th>98</th>
      <td>919854</td>
      <td>2017-05-22 11:44:34</td>
      <td>2017-05-22 12:08:13</td>
      <td>1419</td>
      <td>Montrose Harbor</td>
      <td>Lake Shore Dr &amp; Belmont Ave</td>
      <td>Customer</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5</td>
      <td>Monday</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    import time
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    common_day = df['day_of_week'].mode()[0]
    print('Most common day: ', common_day)

    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]
    print('Most common hour: ', common_hour)

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

```


```python
time_stats(df)
```


    Calculating The Most Frequent Times of Travel...

    Most common month: 5
    Most common day:  Monday
    Most common hour:  17

    This took 0.014252185821533203 seconds.
    ----------------------------------------



```python

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


    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

```


```python
station_stats(df)
```


```python

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    import time

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_trip_duration = df['Trip Duration'].sum()
    print('Total travel time: ', total_trip_duration)


    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time)

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

```


```python
trip_duration_stats(df)
```


```python
def user_stats(df):
    """Displays statistics on bikeshare users.

    """

    print('\nCalculating User Stats...\n')
    import time
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Please see here user types: " + str(user_types))

    # TO DO: Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
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
```


```python
user_stats(df)
```


```python
def view_data(df):
    display = input('Would you like to see the next 5 rows of data? Please select yes or no: ').lower()
    i = 0

    while True:
        print(df.iloc[i:i+5])
        i += 5

        view_more = input('Would you like to see the following 5 rows of data? Please select yes/no').lower()
        if view_more == ('yes'):
            print(df.iloc[i:i+5])
            i += 5     
        else:
            break           

```


```python
view_data(df)
```


```python
def main(df):
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        stations_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('Would you like to end here? Yes or No? ')
        if restart.lower() != 'yes':
            break


```


```python
get_filters()
```


```python

```


```python


```


```python

```


```python

```


```python

```
