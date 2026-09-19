from datetime import date, time, datetime

#calling the day
#function of date class
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent date and time is :", now)


#Printing date's components
print("\nDate components", today.year, today.month, today.day)