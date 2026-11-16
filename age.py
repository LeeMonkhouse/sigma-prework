import datetime
todays_date = datetime.datetime.now()
user_date = input("Please input a date in the following format: dd-mm-yyyy: ")
try:
    user_date = datetime.datetime.strptime(user_date, "%d-%m-%Y")
    difference = todays_date.year - user_date.year
    print(difference, "years")
except ValueError:
    print("Invalid date or format")
