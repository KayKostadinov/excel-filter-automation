from datetime import date
import datetime


class TimeTurner:

    # get the start date for the report
    @staticmethod
    def get_start_date():
        today = date.today()
        today_day_of_week = today.weekday()

        if today_day_of_week == 0:
            return date.today() - datetime.timedelta(days=3)
        return date.today() - datetime.timedelta(days=2)

