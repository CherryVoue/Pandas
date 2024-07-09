"""
Purpose: combine two csv files without merging or removing any fields
Imports: pandas (with openpyxl) to load and parse csv files
Concatenates csv data, aligning columns with matching headers and inserting blanks where headers don't match
"""

#  python 3.12.3
#  pandas 2.2.2
#  openpyxl 3.1.5
import pandas as pd


def concat_csv(file_paths: list[str]) -> None:
    #  Takes a list of file names/paths as a parameter
    #  No return call; combines file data in Excel and ends

    #  Initialize combined list
    data_list = []

    for path in file_paths:
        #  Create dataframe object with csv data
        #  Appends dataframe to the list
        temp_data = pd.read_csv(path)
        data_list.append(temp_data)

    #  Creates pandas dataframe with concatenated sheet data
    concat_df = pd.concat(data_list)

    #  Writes dataframe data to path without an index column
    #  Folder (output) must exist beforehand
    #  Overwrites data if file exists
    concat_df.to_csv('output/combined.csv', index=False)


if __name__ == '__main__':
    #  Add csv file paths to list
    paths = ['data/customers.csv', 'data/people.csv']

    #  Call combine function
    concat_csv(paths)