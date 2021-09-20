import time
import pandas as pd
import numpy as np

# date; 19.september.21 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

#---------------------------------------------------------------------------------------------------------------
def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
     
    while True:
        city = input('would you like to see the data for chicago, new york  or washington? \n').lower()
        if city not in ('chicago', 'new york','washington'):
            print('you enterd an invalid input, try again')
        else: 
            break 
         
    while True:
        month = input('which month? (january, february, ... , june), or type "all" for no month filter \n')
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all' ):
            print('you enterd an invalid input, try again')
        else: 
            break 
   
    while True:
        day = input('which day? (monday, tuesday, ... sunday), or type "all" for no day filters  \n')
        if day.lower() not in ('monday', 'tuesday','wednesday', 'thursday', 'friday	', 'saturday', 'sunday', 'all' ):
            print('you enterd an invalid input, try again')
        else: 
            break 
        
    print('-'*40)
    return city, month, day

#---------------------------------------------------------------------------------------------------------------
def load_data(city, month, day):
   
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day of week'] == day.title()]
 
   
   
    return df

#---------------------------------------------------------------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
   
    # TO DO: display the most common month
    Popular_month = df['month'].mode()[0]
    print('Most Popular month: ', Popular_month)
    print('\n')
    
    # TO DO: display the most common day of week
    popular_day = df['day of week'].mode()[0]
    print('Most Popular day: ', popular_day)
    print('\n')
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:',  popular_hour)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#---------------------------------------------------------------------------------------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', Popular_start_station)
    

    # TO DO: display most commonly used end station
    Popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station: ', Popular_end_station )
    

    # TO DO: display most frequent combination of start station and end station trip
    most_common_routes = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print("most frequent combination of start station and end station trip:\n", most_common_routes)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#---------------------------------------------------------------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time:  ', df['Trip Duration'].sum())
    
    # TO DO: display mean travel time
    print('mean travel time:  ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#---------------------------------------------------------------------------------------------------------------
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('count of user type:  \n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
         print('count of gender:  \n', df['Gender'].value_counts())
         print('earliest year od birth :  ', df['Birth Year'].min())
         print('most recent year of birth :  ', df['Birth Year'].max())
         print('most common year of birth :  ', df['Birth Year'].mode()[0])
    
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#---------------------------------------------------------------------------------------------------------------
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        while view_data == 'yes':
            print(df.iloc[start_loc: start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
        
        

if __name__ == "__main__":
	main()
