"""
Purpose: filter an Excel sheet by given date (year: xxxx, month: xx, day: xx)
Imports: pandas (with openpyxl) to load and parse Excel files
"""

#  python 3.12.3
#  pandas 2.2.2
#  openpyxl 3.1.5
import pandas as pd


def filter_csv(file: str, date_filter: str) -> None:
    #  Takes a list of file names/paths and date filter as parameters
    #  No return call; filters file data in Excel and ends

    #  Reads csv data into dataframe
    df = pd.read_csv(file)

    #  Converts filter to datetime object
    filter_dt = pd.to_datetime(date_filter)

    #  Gets today's date as a count of days since epoch
    today_days = pd.Timestamp.today().floor(freq='D')
    #  Creates a datetime object with
    today_dt = pd.to_datetime(today_days)

    #  Sets csv date column to pandas series object
    sheet_dates = pd.to_datetime(df['Subscription Date'])

    for date in range(len(sheet_dates)):
        #  Gets difference of dates in amount of days
        day_diff = (sheet_dates[date] - filter_dt).days

        if day_diff <= 0:
            #  Drops row from dataframe if date is before filter
            df = df.drop(date)

    #  Writes dataframe data to excel without an index column
    #  Overwrites data if file exists
    df.to_csv('output/customers_filtered.csv', index=False)


if __name__ == '__main__':
    #  Set csv file path to variable
    path = 'data/customers.csv'

    #  Call combine function with date string y-m-d
    filter_csv(path, '2021-01-01')
