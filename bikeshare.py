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

    # Get user input for city (chicago, new york city, washington).
    city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()

    # Handle unexpected input for city
    while city not in CITY_DATA:
        print('Data for the city entered is not available. Please try again.')
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        print('\n')

    # Set checklist for handling unexpected input
    options = ['month','day','both','none']
    months = ['january','february','march','april','may','june']
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    # Get user input for filter by month, day or not at all?
    option = input('Would you like to filter the data by month, day, both or not at all? Enter "None" for no time filter.\n').lower()

    # Handle unexpected input for option
    while option not in options:
        print('It seems that the option entered does not exist. Please try again.')
        option = input('Would you like to filter the data by month, day, both or not at all? Enter "None" for no time filter.\n').lower()

    if option == 'month':

        #set value for day
        day = 'all'

        # Get user input for month (all, january, february, ... , june)
        month = input('Which month - January, February, March, April, May or June? Please type the month in full.\n').lower()

        # Handle unexpected input for month
        while month not in months:
            print('It seems that the month entered does not exist. Please try again.')
            month = input('Which month - January, February, March, April, May or June? Please type the month in full.\n').lower()
        print('\n')

    elif option == 'day':

        #set value for month
        month = 'all'

        # Get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? Please type the day in full.\n').lower()

        # Handle unexpected input for day
        while day not in days:
            print('It seems that the day entered does not exist. Please try again.')
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? Please type the day in full.\n').lower()
        print('\n')

    elif option == 'both':

        # Get user input for month (all, january, february, ... , june)
        month = input('Which month - January, February, March, April, May or June? Please type the month in full.\n').lower()

        # Handle unexpected input for month
        while month not in months:
            print('It seems that the month entered does not exist. Please try again.')
            month = input('Which month - January, February, March, April, May or June? Please type the month in full.\n').lower()
        print('\n')

        # Get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? Please type the day in full.\n').lower()

        # Handle unexpected input for day
        while day not in days:
            print('It seems that the day entered does not exist. Please try again.')
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? Please type the day in full.\n').lower()
        print('\n')

    else: # option for no time filter

        #set value for month and day
        month = 'all'
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
    print('Data loading... Just for a moment...')

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create a month column
    df['month'] = df['Start Time'].dt.month
    # extract month and day of week from Start Time to create a day of week column
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    print('Data loading completed for... \n City: {} \n Month: {} \n Day: {}'.format(city.title(),month,day))
    print('-'*40)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most frequent for ALL months
    if df['month'].nunique() > 1:
        # Display the most common month
        common_month = df['month'].mode()[0]
        count_month = df['month'].value_counts().tolist()[0]
        print('Month: \n{} (Count:{})\n'.format(common_month,count_month))

    # Display the most frequent for month selected
    else:
        # Display the most common month
        common_month = df['month'].mode()[0]
        count_month = df['month'].count()
        print('Month - Filter applied: \n{} (Count:{}) \n'.format(common_month,count_month))

    # Display the most frequent for ALL days
    if df['day_of_week'].nunique() > 1:
        # Display the most common day of week
        common_day = df['day_of_week'].mode()[0]
        count_day = df['day_of_week'].value_counts().tolist()[0]
        print('Day of week: \n{} (Count:{})\n'.format(common_day,count_day))

    # Display the most frequent for day selected
    else:
        # Display the most common day of week
        common_day = df['day_of_week'].mode()[0]
        count_day = df['day_of_week'].count()
        print('Day of week - Filter applied: \n{} (Count:{})\n'.format(common_day,count_day))

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # Display the most common start hour
    common_hour = df['hour'].mode()[0]
    count_hour = df['hour'].value_counts().tolist()[0]
    print('Hour: \n{} (Count:{})\n'.format(common_hour,count_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    count_start = df['Start Station'].value_counts().tolist()[0]
    print('Start Station: \n{} (Count:{})\n'.format(common_start,count_start))

    # Display most commonly used end station
    common_end = df['End Station'].mode()[0]
    count_end = df['End Station'].value_counts().tolist()[0]
    print('End Station: \n{} (Count:{})\n'.format(common_end,count_end))

    # extract start and end station to create a combined start-end station
    df['start_end'] = df['Start Station'] + ', ' + df['End Station']

    # Display most frequent combination of start station and end station trip
    common_start_end = df['start_end'].mode()[0]
    count_start_end = df['start_end'].value_counts().tolist()[0]
    print('Combination of Start Station and End Station: \n{} (Count:{})\n'.format(common_start_end,count_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_time = timedelta(seconds= float(df['Trip Duration'].sum()))
    print('Total Trip Duration: \n{} (HH:MM:SS)\n'.format(total_time))

    # Display mean travel time
    mean_time = timedelta(seconds= float(df['Trip Duration'].mean()))
    print('Average Trip Duration: \n{} (HH:MM:SS) \n'.format(mean_time))

    # Display minimum travel time
    min_time = timedelta(seconds= float(df['Trip Duration'].min()))
    print('Minimum Trip Duration: \n{} (HH:MM:SS) \n'.format(min_time))

    # Display minimum travel time
    max_time = timedelta(seconds= float(df['Trip Duration'].max()))
    print('Maximum Trip Duration: \n{} (HH:MM:SS) \n'.format(max_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    user_types.columns = ['Count']
    print('Distribution based on User Type:')
    print(user_types)
    print('\n')

    if 'Gender' in df.columns:
        # Display counts of gender
        gender = df['Gender'].value_counts().to_frame() #excludes null values
        gender.columns = ['Count']
        print('Distribution based on Gender:')
        print(gender)
        print('\n')

    else:
        print("No available data for 'Gender'\n")

    if 'Birth Year' in df.columns:

        # Display earliest year of birth
        early_year = df['Birth Year'].min()
        early_count = df[df['Birth Year'] == early_year]['Birth Year'].count()
        print('Earliest year of birth: \n{} (Count:{})\n'.format(int(early_year),early_count))

        # Display most recent year of birth
        recent_year = df['Birth Year'].max()
        recent_count = df[df['Birth Year'] == recent_year]['Birth Year'].count()
        print('Most recent year of birth: \n{} (Count:{})\n'.format(int(recent_year),recent_count))

        # Display most common year of birth
        common_year = df['Birth Year'].mode()[0]
        common_count = df[df['Birth Year'] == common_year]['Birth Year'].count()
        print('Most common year of birth: \n{} (Count:{})\n'.format(int(common_year),common_count))

    else:
        print("No available data for 'Birth Year'\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    # Get user input for displaying raw data
    options = ['yes', 'no']
    option = input("Would you like to see the raw data? Enter 'Yes' or 'No'\n").lower()

    # Handle unexpected input for option
    while option not in options:
        print('It seems that the option entered does not exist. Please try again.')
        option = input("Would you like to see the raw data? Enter 'Yes' or 'No'\n").lower()

    if option == 'yes':

        print('Loading raw data...\n')
        # drop columns not in raw data
        df = df.drop([df.columns[-2],df.columns[-1]], axis =1).rename(columns={'Unnamed: 0': ''})
        df_listed = df.to_dict('records') # convert to list

        # initialize variables
        count = 0    #counter
        N = 5  #limit

        outputs = df_listed[count:(count+N)]
        for output in outputs:
            print(output)
        print('\n')

        # Get user input for displaying more raw data
        option_more = input("Would you like to see more raw data? Enter 'Yes' or 'No'\n").lower()

        # Handle unexpected input for option to load more raw data
        while option_more not in options:
            print('It seems that the option entered does not exist. Please try again.')
            option_more = input("Would you like to see more raw data? Enter 'Yes' or 'No'\n").lower()

        # Loop and print N inputs each time
        while option_more != 'no':
            count += N
            outputs = df_listed[count:(count+N)] # slice through the list to display N inputs
            for output in outputs:
                print(output)
            print('\n')

            # Breaks the loop if last dataset has been displayed
            if count+N > len(df_listed):
                break
            # else continue viewing data
            else:
                option_more = input("Would you like to see more raw data? Enter 'Yes' or 'No'\n").lower()

                while option_more not in options:
                    print('It seems that the option entered does not exist. Please try again.')
                    option_more = input("Would you like to see more raw data? Enter 'Yes' or 'No'\n").lower()

        print('\n Viewing of raw data completed...\n')
        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print('\nEnd of statistical analysis.\n')
        print('-'*40)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        print('='*80)
        if restart.lower() != 'yes':
            print("\nHave a nice day! Goodbye!\n")
            break

if __name__ == "__main__":
    main()
