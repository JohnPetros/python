# Datetime Module

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Get current date and time
current_datetime = datetime.now()
print("Current Date and Time =", current_datetime)

# Get current date
current_date = datetime.now().date()
print("Current Date =", current_date)

# Get current time
current_time = datetime.now().time()
print("Current Time =", current_time)

# Add 7 days to the current date
future_date = current_date + timedelta(days=7)
print("Date after 7 days =", future_date)

# Subtract 3 hours from the current time
past_time = current_time - timedelta(hours=3)
print("Time 3 hours ago =", past_time)

# Format date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time =", formatted_datetime)

# Parse date and time from string
parsed_datetime = datetime.strptime("2022-12-31 23:59:59", "%Y-%m-%d %H:%M:%S")
print("Parsed Date and Time =", parsed_datetime)


# Get current date and time in UTC
utc_now = datetime.now(ZoneInfo("UTC"))
print("Current Date and Time in UTC =", utc_now)

# Convert to New York time
ny_now = utc_now.astimezone(ZoneInfo("America/New_York"))
print("Current Date and Time in New York =", ny_now)

# Convert to Tokyo time
tokyo_now = utc_now.astimezone(ZoneInfo("Asia/Tokyo"))
print("Current Date and Time in Tokyo =", tokyo_now)

# Convert back to UTC
utc_now_again = ny_now.astimezone(ZoneInfo("UTC"))
print("Converted Date and Time back to UTC =", utc_now_again)
