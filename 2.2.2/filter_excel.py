"""
Purpose: filter a Excel sheet by given date (year: xxxx, month: xx, day: xx)
Imports: pandas (with openpyxl) to load and parse Excel files
"""

#  python 3.12.3
#  pandas 2.2.2
#  openpyxl 3.1.5
import pandas as pd


def filter_excel(file: str, date_filter: str) -> None:
    #  Takes a list of file names/paths and date filter as parameters
    #  No return call; filters file data in Excel and ends

    #  Reads Excel data into pandas excel file object
    excel_file = pd.ExcelFile(path)

    #  Excel file object to dataframe (default first sheet)
    df = excel_file.parse(sheet_name=0)

    #  Converts filter to datetime object
    filter_dt = pd.to_datetime(date_filter)

    #  Sets Excel date column to pandas datetime object
    sheet_dates = pd.to_datetime(df['Date of Release'])

    for date in range(len(sheet_dates)):
        #  Gets difference of dates in amount of days
        day_diff = (sheet_dates[date] - filter_dt).days

        if day_diff <= 0:
            #  Drops row from dataframe if date is before filter cutoff
            df = df.drop(date)

    #  Writes dataframe data to Excel without an index column
    #  Overwrites data if file exists
    df.to_excel('output/file1_filtered.xlsx', index=False)


if __name__ == '__main__':
    #  Set Excel file path to variable
    path = 'data/file1.xlsx'

    #  Call combine function with date string y-m-d
    filter_excel(path, '2021-01-01')
