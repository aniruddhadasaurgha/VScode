import datetime
import calendar

current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

print("The calendar for the current year is : ",calendar.calendar(2025))

print("-------------")

week_calendar = calendar.TextCalendar(calendar.SUNDAY)
print(week_calendar.formatyear(2025))