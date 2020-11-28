# Python to find day of the week that given date

import re # regular expression
import calendar # module of python to provide useful function related to calendar
import datetime # module of python to get the date and time

def process_date(user_input):
    user_input = re.sub(r"/", " ", user_input) #substitube/ with space
    user_input = re.sub (r"-"," ", user_input)
    return user_input
def find_day(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])

user_input = str(input("enter date      "))
date = process_date(user_input)
print("Day on" + user_input + "is " + find_day(date))