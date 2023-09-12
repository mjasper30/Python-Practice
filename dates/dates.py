import datetime

date_now = datetime.datetime.now()

print(date_now.year)  # Prints Year Today - ex 2023
print(date_now.strftime("%A"))  # Prints Day Today - ex Tuesday
# Prints the whole data in number format - ex 2023-09-12 11:12:03.248102
print(date_now)

# Goal : Print in this format - Month Day, Year
month = date_now.strftime("%B")
day = date_now.strftime("%d")
year = date_now.strftime("%Y")

print(f"{month} {day}, {year}")  # OUTPUT: September 12, 2023

"""
More info on how you can show you want to show
https://www.w3schools.com/python/python_datetime.asp
"""
