import calendar

import time


def create_time_stamp(date_string, formatting="%Y-%m-%d %H:%M:%S"):
    """
    Sometimes Poloniex will return a date as a string. This converts it to
    a timestamp.
    
    Args:
        date_string: Date string returned by poloniex
        formatting: The default format poloniex returns the date_string in

    Returns:
        UNIX timestamp

    """
    return calendar.timegm(time.strptime(date_string, formatting))
