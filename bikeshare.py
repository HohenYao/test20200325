import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#add month_list, DayOfWeek_list by Hohen
month_list = ['january', 'feburary', 'march', 'april', 'may', 'june']
DayOfWeek_list = { 1:'sunday', 2:'monday', 3:'tuesday', 4:'wednesday', 5:'thursday', 6:'friday', 7:'saturday'}

def check_month():
        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:            
            month = input('Enter the month you want to check, January, Feburary, ..., June: ').lower()
            if (month in month_list):
                break
            else:
                print("The month you input is invalid ")
        except ValueError:
            print('That\'s not a valid month! ')
        except KeyboardInterrupt:
            print('\nNo input taken ')
            break
        finally:
            print('\nAttempted Input\n ')
    
    return month
            
def check_day_of_week():
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day_num = int(input('Enter the day of week you want to check, using an integer, 1=Sunday, 2=Monday, ...7=Saturday: '))
            
            if DayOfWeek_list.get(day_num):
                day = DayOfWeek_list[day_num]
                break
            else:
                print("The day of week you input is invalid ") 
        except ValueError:
            print('That\'s not a valid day of week! ')
        except KeyboardInterrput:
            print('\nNo input taken ')
            break
        finally:
            print('\nAttempted Input\n ')
            
    return day

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
        try:
            city = input('Enter the city you want to check, Chicago, New York City or Washington: ').lower()
            if CITY_DATA.get(city):
                break
            else:
                print("You only can input 'Chicago, New York City or Washington' ")
        except ValueError:
            print("That\'s not a valid city name! ")
        except KeyboardInterrupt:
            print('\nNo input taken ')
            break
        finally:
            print('\nAttempted Input\n')            
            
    while True:
        filter_type = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n').lower()

        if filter_type == 'none':
            month='all'
            day='all'
            print("filter type is: {} ".format(filter_type))
            break
        elif filter_type == 'both':
            month=check_month()
            day=check_day_of_week()
            print("filter type is: {} (month and day)".format(filter_type))
            break
        elif filter_type == 'month':
            month=check_month()
            day='all'
            print("filter type is: {} ".format(filter_type))
            break
        elif filter_type == 'day':
            month='all'
            day=check_day_of_week()
            print("filter type is: {} ".format(filter_type))
            break
        else:
            print ('Sorry, please give a valid input')
            
    
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
    #add by Hohen, take practise 3 as a reference
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'feburary', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #add by Hohen, take practise 1 as reference
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])   
        
    # TO DO: display the most common month
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    
    # find the most popular month
    popular_month = df['month'].mode()[0]
    #popular_month_count = df['month'].value_counts()[popular_month_count]

    print('Most Popular month: {} '.format(popular_month))
    #print('Most Popular Start month: {}, count: {} '.format(popular_month, popular_month_count))
                        
    # TO DO: display the most common day of week
    # extract day_of_week from the Start Time column to create an hour column
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # find the most popular day_of_week
    popular_day_of_week = DayOfWeek_list.get(df['day_of_week'].mode()[0]).title()

    print('Most Popular day of week: {}'.format(popular_day_of_week))

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    popular_hour_count = df['hour'].value_counts()[popular_hour]
        
    print('Most Popular Hour: {}, Count:{} '.format(popular_hour, popular_hour_count))
                        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    '''add by Hohen, take practise 2 and "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.value_counts.html", "https://www.jianshu.com/p/f773b4b82c66", "https://www.cnblogs.com/keye/p/9664414.html" as reference'''
    # TO DO: display most commonly used start station
       
    # counts for most commonly used start station
    commonly_start_station = df['Start Station'].value_counts().index[0]
    #commonly_start_station_count = df['Start Station'].value_counts().data[0]
    commonly_start_station_count = df['Start Station'].value_counts()[commonly_start_station]
    
    print('Most commonly used start station:{}, count: {} '.format(commonly_start_station, commonly_start_station_count))

    # TO DO: display most commonly used end station
    # counts for most commonly used end station
    commonly_end_station = df['End Station'].value_counts().index[0]
    commonly_end_station_count = df['End Station'].value_counts()[commonly_end_station]
    
    print('Most commonly used end station:{}, count: {} '.format(commonly_end_station, commonly_end_station_count))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_of_trip'] = df['Start Station']+ ' To ' + df['End Station']
    frequent_combine = df['combination_of_trip'].value_counts().index[0]
    frequent_combine_count = df['combination_of_trip'].value_counts()[frequent_combine]
    print('Most frequent combination of start station and end station trip:{}, count:{} '.format(frequent_combine, frequent_combine_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is: {} seconds".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Average travel time is: {} seconds".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #added by Hohen, take practise 2 as reference
    # TO DO: Display counts of user types
    columns_in_city = df.columns

    user_types = df['User Type'].value_counts()
    print(user_types)
    
    # TO DO: Display counts of gender
    if 'Gender' in columns_in_city:
        Gender = df['Gender'].value_counts()
        print(Gender)
    else:
        print("Sorry, there is no gender data in this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in columns_in_city:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].value_counts().index[0]
        print("The earliest year of birth among users is {} ".format(earliest_birth))
        print("The most recent year of birth among users is {} ".format(most_recent_birth))
        print("The most common year of birth among users is {} ".format(most_common_birth))
    else:
        print("Sorry, there is no birth year data in this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
'''
#this is used for the first 5 records
def show_info(df):
    """Displays several detail on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    #show several detail
    info = df.head()
    record_num = 5

    print("There are five records for your reference :\n {}".format(info))
    
    while True:
        try:
            read_more = input('Would you like to see more records?(yes or no, y or n ) : ').lower()
            if (read_more == 'no' or read_more == 'n'):
                break
            elif (read_more == 'yes' or read_more == 'y'):
                record_num +=5
                info = df.head(record_num)
                print("There are some records for your reference :\n {}".format(info))
            else:
                print("Your input is invalid ")                 
        except ValueError:
            print("That\'s not a valid input! ")
        except KeyboardInterrupt:
            print('\nNo input taken ')
            break
        finally:
            print('\nAttempted Input\n')    
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

'''
def show_info(df):
    """Displays several detail on bikeshare users."""

    #add by Hohen, take "https://www.jb51.net/article/143587.htm" as a reference
    # load data file into a dataframe

    print('\nCalculating show_info...\n')
    
    
    #show several detail
    record_num = 0
           
    while True:
        try:
            start_time = time.time()
            info = df[ record_num : record_num + 5 ]
            print("There are some records for your reference :\n {}".format(info))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            read_more = input('Would you like to see more records?(yes or no, y or n ) : ').lower()
            if (read_more == 'no' or read_more == 'n'):
                break
            elif (read_more == 'yes' or read_more == 'y'):
                record_num += 5
            else:
                print("Your input is invalid ")                 
        except ValueError:
            print("That\'s not a valid input! ")
        except KeyboardInterrupt:
            print('\nNo input taken ')
            break
        finally:
            print('\nAttempted Input\n')    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_info(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
