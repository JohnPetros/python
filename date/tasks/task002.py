# Task 2 - A company wants to display the current time on its website in the format: "Day of the week, day of the mounth, hours: minutes". Write a script that displays the current time in this Format. After that format it into Brazil's zone time

import time
import locale

current_time = time.localtime()

print(time.strftime("%A, on %B %d at %H:%M", current_time))

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

print(time.strftime("%A, %d de %B as %H:%M", current_time))
