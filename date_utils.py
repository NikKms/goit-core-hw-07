from datetime import datetime, timedelta

class DateUtils:
    @staticmethod
    def get_next_weekday(date, weekday):
        days_ahead = (weekday - date.weekday() + 7) % 7
        return date + timedelta(days=days_ahead or 7)

    @classmethod
    def adjust_for_weekend(cls, date):
        if date.weekday() >= 5:
            return cls.get_next_weekday(date, 0)
        return date

    @staticmethod
    def format_date(date):
        return date.strftime("%d.%m.%Y")

    @staticmethod
    def parse_date(date_str, date_format='%d.%m.%Y'):
        return datetime.strptime(date_str, date_format)
