import calendar

age = int(input("Age: "))
month = int(input("month of birth (1-12): "))
date = int(input("date of birth (1-31): "))
current_year = int (input("current year: "))

year = current_year - age
day = calendar.weekday(year,month,date)
day_string = calendar.day_name[day]

print("you were born on a " + day_string + " in the year " + str(year))
