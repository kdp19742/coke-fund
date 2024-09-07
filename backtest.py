import pandas as pd
import numpy as np
import yfinance as yf


def first_monday_after_labor_day(year):
    return np.busday_offset(
        f'{year}-09',
        1,
        roll='forward',
        weekmask='Mon'
    )

ticker = yf.Ticker('SPY')
spy = ticker.history(period="max")
spy = spy.drop(['Dividends','Stock Splits','Capital Gains'], axis=1)
spy = spy.reset_index()

spy['year'] = spy['Date'].dt.year
year = spy.iloc[0].at['year']
monday = first_monday_after_labor_day(year)
week_after_labor_day = spy.loc[
    (spy['Date'].dt.month==9) &
    (spy['Date'].dt.date >= monday) &
    (spy['Date'].dt.date <= monday+4)
]
print(week_after_labor_day)

beg_week_open = (week_after_labor_day.iloc[0].at['Open'])
end_week_close = (week_after_labor_day.iloc[-1].at['Close'])
nominal_change = end_week_close-beg_week_open
percentage_change = 100*(end_week_close/beg_week_open-1)
print(f'Monday Open Price: {beg_week_open}\nFriday Close Price: {end_week_close}')
print(f'Weekly Nominal Change: {nominal_change}\nWeekly Percentage Change: {percentage_change}')




#spy['year'] = spy['Date'].apply(lambda x: x.strftime('%Y'))
# sep = spy[((spy['Date'].index.month == 9) & (spy['Date'].index.day > 5))]
# print(sep)

# print(spy)
# septembers = spy[spy['Date'].dt.strftime('%m-%d-%Y').str.startswith('09')]
# sep_1993 = septembers[0:21]
# print(sep_1993)
# print(sep_1993.iloc[7].at['Date'])

# from pandas.tseries.holiday import USFederalHolidayCalendar
# holiday_cal = USFederalHolidayCalendar()
# spy['Date'] = spy['Date'].dt.date
# holiday_cal = USFederalHolidayCalendar()
# holidays = holiday_cal.holidays()
# custom_bday = pd.offsets.CustomBusinessDay(holidays=holidays)
# print(custom_bday)

# holiday_cal = USFederalHolidayCalendar()
# holidays = holiday_cal.holidays(start=sep_1993.iloc[0].at['Date'],end=sep_1993.iloc[-1].at['Date'])
# custom_bday = pd.offsets.CustomBusinessDay(holidays=holidays)
# print(sep_1993.iloc[2].at['Date'] + custom_bday)

# spy = pd.read_csv('historical_spy_daily_ohlc.csv')
# print(spy)

# plot = septembers.plot(title='Septembers')
# print(septembers.groupby(septembers['date'].dt.year))
# print(septembers)

# september['week'] = september['date'].dt.isocalendar().week
# spy['week'] = spy['date'].dt.isocalendar().week
# print(september)

# for i in spy:
#     if spy['date'].dt.month == 9:
#         print(i)
# september = pd.date_range(spy['date'].head, spy['date'].tail, freq='MS')
# print(september)

# conditions = [
#     (spy['date'].)
# ]