# pcostcommand.py
#
# Exercise 1.33

import sys

def portfoliocost(filename):
    runningTotal = 0.0
    with open(filename,'rt') as file: # Open the file, if leaving the block it will automatically close
        headers = next(file) # Skip the first line in the file

        for line in file: # for each line in the file
            row= line.split(',') # Then split the line into a list
            try:
                runningTotal += float(row[1]) * float(row[2]) # Num shares * cost of each share added into a running total
            except ValueError: # If rows could not be processed for values, raise exception and continue processing value
                print('Could not parse value. Skipping row and continuing.')
                continue
    return runningTotal
    
if len(sys.argv) == 2: # python pcostcommmand.py Data/portfolio.csv
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfoliocost('Data/portfolio.csv')
print('Total:', cost)