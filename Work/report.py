# report.py
#
# Exercise 2.4
import csv

portfolio = []
prices = {}
total_cost = 0.0

def read_portfolio(filename):
    with open(filename,'rt') as file: # Open the file, if leaving the block it will automatically close
        rows = csv.reader(file) #csv.reader splits file into lists named rows
        headers = next(rows) # Skip the first row

        for row in rows: # for each list named row
            # holding = (row[0],int(row[1]), float(row[2]))
            # portfolio.append(holding)
            stock = { #List of dictionaries
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(stock)
    return portfolio

def read_prices(filename):
     with open(filename,'rt') as file: # Open the file, if leaving the block it will automatically close
        rows = csv.reader(file) #csv.reader splits file into lists named rows
        headers = next(rows) # Skip the first row

        for row in rows: # for each list named row
            try: 
                prices[row[0]] = float(row[1]) # Set
            except IndexError:
                pass
                
     return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Calculate the totcal cost of the portfolio
for p in portfolio:
    total_cost += p['shares']*p['price']

#Calculate the total value of the portfolio based on stock name
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value:', total_value)
print('Gain/Loss:', total_value - total_cost)
    