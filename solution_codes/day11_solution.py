#calculating seconds in a year
minutes_in_an_hour = 60
seconds_in_a_minute = 60
seconds_in_an_hour = minutes_in_an_hour * seconds_in_a_minute
seconds_in_a_day = seconds_in_an_hour * 24
seconds_in_a_year = seconds_in_a_day * 365
leap = input('Is it a leap year')
if leap == 'yes':
    print(seconds_in_a_day * 366)
else:
    print(seconds_in_a_year)
