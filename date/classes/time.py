import time
import locale

# Set locale to French
locale.setlocale(locale.LC_ALL, "fr_FR")

# Get current time
current_time = time.time()
print("Current Time =", current_time)

# Get local time
local_time = time.localtime(time.time())
print("Local Time =", local_time)

# Print type of local_time
print("Type of Local Time =", type(local_time))

# Access elements of local_time
print("Year =", local_time.tm_year)
print("Month =", local_time.tm_mon)
print("Day =", local_time.tm_mday)
print("Hour =", local_time.tm_hour)
print("Minute =", local_time.tm_min)
print("Second =", local_time.tm_sec)

# Format local time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted Local Time =", formatted_time)

# Delay execution
print("Waiting for 5 seconds...")
time.sleep(5)
print("Done waiting!")

# Measure execution time
start_time = time.time()
for i in range(10000):
    pass
end_time = time.time()
execution_time = end_time - start_time
print("Execution Time =", execution_time)
