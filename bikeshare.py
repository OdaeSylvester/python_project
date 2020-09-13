import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago','new york city', 'washington']
months = ['january','february','march','april','may','june','all']
days =['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
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
        city = input('\n Would you like to see data for Chicago, New York or Washington? ')
        city = city.lower()
        if city in cities:
                     break
        else:
                     print('Enter a valid city')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month do you want to filter?\n January, Febuary, March, April, May, June or All:  ')
        month = month.lower()
        if month in months:
                      break
        else :
                      print('Enter a valid month')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day of the week do you want to filter?\n Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All: ')
        day = day.lower()
        if day in days:
                    break
        else:
                    print('Enter a valid day')

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
    # Assign a variable file_name to file to be loaded based on the city chosen
    file_name = CITY_DATA[city]
    
    # load file into Data Frame
    df = pd.read_csv(file_name)
    
   # convert the Start Time column to datetime
    df['Start Time']= pd.to_datetime(df['Start Time'])
   
   #filter by month
   # Create column for month from the Start Time column
    df['month'] = df['Start Time'].dt.month
   
  # filter by month if applicable
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        
  # filter by month to create the new dataframe
    df =df[df['month'] == month]
  
  # filter by day of the week
  # Create column for day of the week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
  
  # filter by day of the week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
                        
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    datetime_object = datetime.datetime.strptime(str(common_month),"%m")
    month_name= datetime_object.strftime("%B")
    month_count = df['month'].value_counts().max()
    print('Most common month is {}, and count is {} '.format(month_name, month_count))
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    common_day_count = df['day_of_week'].value_counts().max()
    print('Most common day of the week is {} and count is {} '.format(common_day, common_day_count))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    common_hour_count = df['hour'].value_counts().max()
    print('Most common hour is {} and count is {}'.format(common_hour, common_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    common_start_station_count = df['Start Station'].value_counts().max()
    print('Most commonly used start station is: {}'.format(common_start_station, common_start_station_count))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    common_end_station_count = df['End Station'].value_counts().max()
    print('\nMost commonly used end station is {} and count is {}'.format(common_end_station, common_end_station_count))

    # TO DO: display most frequent combination of start station and end station trip
    combined_stations = df['Start Station'] + " " + df['End Station'] 
    common_combined_stations = combined_stations.value_counts().idxmax()
    common_combined_stations_count = combined_stations.value_counts().max()
    print('\nMost common combined stations is {} and count is {}'.format(common_combined_stations, common_combined_stations_count ))                                                   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {}'.format(total_travel_time))                                                   
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is: {}'.format(mean_travel_time))                                                 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user type are:\n',user_types)
    
    # Most common user type
    most_common_user = user_types.idxmax()
    print('\nMost common user type is: {}'.format(most_common_user))                                                  

    # TO DO: Display counts of gender
    if city == 'washington':
        print('There is no record of gender for {}'.format(city))
    else: # display gender counts
        gender_counts = df['Gender'].value_counts()
        print('\nGender counts are:\n', gender_counts)
                                                                  
    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('There is no record of Birth Year for {}'.format(city))
    else:
        # Earliest year of birth
        earliest_birth_year = int(sorted(df.groupby(df['Birth Year'])['Birth Year'])[0][0])
                                                       
    # Most recent year of birth
        recent_birth_year = int(sorted(df.groupby(df['Birth Year'])['Birth Year'], reverse= True)[0][0])
       
    # Most common year of birth
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nThe earliest, most recent and most common year of birth are {}, {}, {}, respectively'.format(earliest_birth_year, recent_birth_year, common_birth_year))                                                  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Display of 5 lines raw data if the user enters yes
    number_rows = 1
    while True:
        data = input('\n Would you like to see 5 lines of raw data?\n Enter Yes or No: ')
        data = data.lower()
        if data == 'yes':
            print(df[number_rows:number_rows+5])
            number_rows +=5
        elif data == 'no':
            break
        else:
            print('\n Enter a valid response')
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
