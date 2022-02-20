# pcostenum.py
#
# Exercise 2.15

import csv #csv library

def portfoliocost(filename):
    runningTotal = 0.0

    with open(filename,'rt') as file: # Open the file, if leaving the block it will automatically close
        rows = csv.reader(file) #csv.reader splits file into lists named rows
        headers = next(rows) # Skip the first row

        for rowno, row in enumerate(rows,start = 1): # for each list named row
            try:
                runningTotal += float(row[1]) * float(row[2]) # Num shares * cost of each share added into a running total
            except ValueError: # If rows could not be processed for values, raise exception and continue processing value
                 print(f'Row {rowno}: Bad row: {row}')
                 continue
    return runningTotal

cost = portfoliocost('Data/portfolio.csv')
print('Total:', cost)
