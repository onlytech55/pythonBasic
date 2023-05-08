### Dates ###

from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()

print(timestamp)

# datetime parámetros mínimos año, mes, dia

year_2023 = datetime(2023, 1, 1)
def print_date(date) :
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
print_date(year_2023)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Modificaciones sobre fechas?

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date)
print(current_date.month)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

# diff = year_2023.time() - current_date   No funciona
# print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(200, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)






