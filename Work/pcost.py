# pcost.py
#
# Exercise 1.27
runningTotal = 0.0
with open('Data/portfolio.csv','rt') as file: # Open the file, if leaving the block it will automatically close
    headers = next(file) # Skip the first line in the file

    for line in file: # for each line in the file
        print(line, end='') # print the line
        row = line.split(',') # Then split the line into a list
        runningTotal += float(row[1]) * float(row[2]) # Num shares * cost of each share added into a running total

    print('Total:',runningTotal) # print running total



