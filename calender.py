from persiantools.jdatetime import JalaliDate
from datetime import datetime
from convertdate import persian, islamic


class Date:
    def __init__(self, input_date):
        self.date = input_date

    @classmethod
    def from_string(cls, input_date):
        """
        Class method to create a Date instance from a string formatted as YYYY-MM-DD.
        """

        from_str = datetime.strptime(input_date, "%Y-%m-%d")
        return cls(from_str)

    @staticmethod
    def is_valid_date(input_date):
        """
        Static method to validate if the date string is in the correct format YYYY-MM-DD.
        """

        from_str = datetime.strptime(input_date, "%Y-%m-%d")
        if isinstance(from_str, datetime):
            return True
        return False

    @staticmethod
    def to_shamsi(input_date):
        """
        Static method to convert a Gregorian date to Shamsi date with convertdate library .
        """

        shamsi = persian.from_gregorian(
            input_date.year, input_date.month, input_date.day
        )
        return shamsi

    @staticmethod
    def to_shamsi_1(input_date):
        """
        Static method to convert a Gregorian date to Shamsi date with JalaliDate library .
        """

        shamsi = JalaliDate(input_date)
        return shamsi

    @staticmethod
    def to_gamari(input_date):
        """
        Static method to convert a Gregorian date to Ghamary date with convertdate library .
        """

        ghamary = islamic.from_gregorian(
            input_date.year, input_date.month, input_date.day
        )
        return ghamary


input_date = input("Enter your date:YYYY-MM-DD ")
try:
    if Date.is_valid_date(input_date):
        d = Date.from_string(input_date)
        print(f"date_to_shamsi: {Date.to_shamsi(d.date)}")
        print(f"date_to_shamsi: {Date.to_shamsi_1(d.date)}")
        print(f"date_to_ghamary: {Date.to_gamari(d.date)}")
    else:
        print("Date validation failed ")
except Exception as e:
    print(e)
