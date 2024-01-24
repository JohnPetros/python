# Task 5 - A company have offices in São Paulo, New York and Tokyo. Write a script that displays the current date and time in these time zones. Also display whether or not these offices are closed or open (9am to 5pm).

from datetime import datetime
from zoneinfo import ZoneInfo

current_date = datetime.today()


sao_paulo_date = current_date.astimezone(ZoneInfo("America/Sao_Paulo"))
new_york_date = current_date.astimezone(ZoneInfo("America/New_York"))
tokyo_date = current_date.astimezone(ZoneInfo("Asia/Tokyo"))

print(sao_paulo_date)
print(new_york_date)
print(tokyo_date)

dates = {
    "São Paulo Office": sao_paulo_date,
    "New York Office": new_york_date,
    "Tokyo Office": tokyo_date,
}

for office, date in dates.items():
    if date.hour >= 9 and date.hour <= 17:
        print(f"{office} is open")
    else:
        print(f"{office} is closed")
