# Task 3 - Write a script that calculates the amount of days, hours and seconds until the next New Year's Eve Day

import time

next_year = time.localtime().tm_year + 1

new_year_first_date = f"01/01/{next_year}"
new_year_first_date_in_struct_time = time.strptime(new_year_first_date, "%m/%d/%Y")
new_year_first_date_in_time = time.mktime(new_year_first_date_in_struct_time)

current_time = time.time()

difference_time = new_year_first_date_in_time - current_time

difference_time_in_struct = time.localtime(difference_time)

days = difference_time_in_struct.tm_yday
hours = difference_time_in_struct.tm_hour
minutes = difference_time_in_struct.tm_min
seconds = difference_time_in_struct.tm_sec

print(f"{days} days and {hours}:{minutes}:{seconds} left until {next_year}")
time.sleep(1)
