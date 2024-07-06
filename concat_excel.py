"""
Purpose: combine two Excel files without merging or removing any fields
Imports: pandas (with openpyxl) to load and parse Excel files
Concatenates Excel data, aligning columns with matching headers and inserting blanks where headers don't match
"""

#  python 3.12.3
#  pandas 2.2.2
#  openpyxl 3.1.5
import pandas as pd


def combine_files(file_paths: list[str]) -> None:
    #  Takes a list of file names/paths as a parameter
    #  No return call; combines file data in Excel and ends

    #  Initialize combined list
    data_list = []

    for path in file_paths:
        #  Create Excel object with file path
        #  Parse file data (defaults to first sheet in Excel)
        #  Appends file data to the list
        temp = pd.ExcelFile(path)
        data = temp.parse(sheet_name=0)
        data_list.append(data)

    #  Creates pandas dataframe with concatenated sheet data
    concat_df = pd.concat(data_list)

    #  Writes dataframe data to path without an index column
    #  Folder (output) must exist beforehand
    #  Overwrites data if file exists
    concat_df.to_excel('output/combined.xlsx', index=False)


if __name__ == '__main__':
    #  Add Excel file paths to list
    paths = ['data/file1.xlsx', 'data/file2.xlsx']

    #  Call combine function
    combine_files(paths)
