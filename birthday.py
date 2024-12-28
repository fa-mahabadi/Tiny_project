from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

class Birthday:
    def __init__(self, date_input):
        self.date_input = date_input

    def age_with_datetime(self):
        """calculate age with datetime module"""
        date_input = datetime.strptime(self.date_input, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        difference = relativedelta(now, date_input)
        return f"your age is: {difference.years} years, {difference.months} months, {difference.days} days, {difference.hours} hours, {difference.minutes} minutes, {difference.seconds} seconds"

    def is_leap_year(self, year):
        """Check if a year is a leap year"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, month, year):
        """return the number of days in a month with consider leap year"""
        if month == 1:
            return 31
        if month == 2:
            return 29 if self.is_leap_year(year) else 28
        if month == 3:
            return 31
        if month == 4:
            return 30
        if month == 5:
            return 31
        if month == 6:
            return 30
        if month == 7:
            return 31
        if month == 8:
            return 31
        if month == 9:
            return 30
        if month == 10:
            return 31
        if month == 11:
            return 30
        if month == 12:
            return 31

    def age_with_time(self):
        """calculate age with time module"""
        p = time.strptime(self.date_input, "%Y-%m-%d %H:%M:%S")
        t = time.localtime()

        year_diff = t.tm_year - p.tm_year
        month_diff = t.tm_mon - p.tm_mon
        day_diff = t.tm_mday - p.tm_mday
        hour_diff = t.tm_hour - p.tm_hour
        minute_diff = t.tm_min - p.tm_min
        second_diff = t.tm_sec - p.tm_sec

        if second_diff < 0:
            second_diff += 60
            minute_diff -= 1

        if minute_diff < 0:
            minute_diff += 60
            hour_diff -= 1

        if hour_diff < 0:
            hour_diff += 24
            day_diff -= 1

        if day_diff < 0:
            previous_month = t.tm_mon - 1 if t.tm_mon > 1 else 12
            previous_year = t.tm_year if t.tm_mon > 1 else t.tm_year - 1
            days_in_previous_month = self.days_in_month(previous_month, previous_year)
            day_diff += days_in_previous_month
            month_diff -= 1

        if month_diff < 0:
            month_diff += 12
            year_diff -= 1

        return f"Your age is: {year_diff} years, {month_diff} months, {day_diff} days, {hour_diff} hours, {minute_diff} minutes, {second_diff} seconds"

    def remain_time_to_birthday(self):
        """calculate remain months,days and hours to birthday"""
        birthday = time.strptime(self.date_input, "%Y-%m-%d %H:%M:%S")
        current_time = time.localtime()
        days_diff = birthday.tm_yday - current_time.tm_yday
        hour_diff = birthday.tm_hour - current_time.tm_hour
        if days_diff > 186:
            mon_diff = 186 // 31
            day_diff = 186 % 31
            days_diff -= 186
            mon_diff += days_diff // 30
            day_diff += days_diff % 30
        elif 0 <= days_diff < 186:
            mon_diff = days_diff // 31
            day_diff = days_diff % 31
        elif days_diff < 0:
            days_diff = 365 + days_diff
            if days_diff > 186:
                mon_diff = 186 // 31
                day_diff = 186 % 31
                days_diff -= 186
                mon_diff += days_diff // 30
                day_diff += days_diff % 30
            elif days_diff < 186:
                mon_diff = days_diff // 31
                day_diff = days_diff % 31
        if hour_diff < 0:
            hour_diff = 24 + hour_diff
            day_diff -= 1

        return f"remain to birthday {mon_diff} months {day_diff} days {hour_diff} hours"


birthday = input("Enter your birthday with this format YYYY-MM-DD HH:MM:SS: ")
b = Birthday(birthday)
print(b.age_with_datetime())
print(b.age_with_time())
print(b.remain_time_to_birthday())
