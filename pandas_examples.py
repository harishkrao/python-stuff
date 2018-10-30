import pandas as pd
from pandas.tseries.offsets import *


def week_of_quarter(timestamp):
    return 'week_' + str(int(pd.to_datetime(timestamp).strftime('%U')) - int(quarter_start_date.strftime('%U')) + 1)


today = pd.to_datetime('today')

print('today {}'.format(today))
end_date = today - DateOffset(days=today.weekday() + 1)
print('end_date {}'.format(end_date))

start_date = end_date - DateOffset(weeks=2)
print('start_date {}'.format(start_date))

start = pd.to_datetime(end_date) - DateOffset(days=1)

quarter_start_date = QuarterEnd().rollback(pd.to_datetime(end_date)) + DateOffset(days=1)

current_week = week_of_quarter(pd.to_datetime(end_date) - DateOffset(weeks=1))

print('start {}'.format(start))
print('quarter_start_date {}'.format(quarter_start_date))
print('current_week {}'.format(current_week))
