# mortgage.py
#
# Exercise 1.7, 1.8, 1.9, 1.10, 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

# Extra payment calculator
extra_payment_start_month = 61 
extra_payment_end_month = 108
extra_payment = 1000

# Used if the next payment is an overpayment
leftover_amount = 0

while principal > 0:
    months = months + 1
    if months <= extra_payment_end_month and months >= extra_payment_start_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment

    leftover_amount = principal # Hold value of principal if next time around is overpayment
    principal = principal * (1+rate/12) - total_payment
    
    if principal < 0: # Since next mortgage payment is overpayment
        total_paid = total_paid + leftover_amount # Final payment should only be leftover amount
        principal = 0
    else:
        total_paid = total_paid + total_payment

    print(f'{months}, ${total_paid:0.2f}, ${principal:0.2f}')
       

print('Total paid:', f'${total_paid:0.2f}')
print('Months: ', months)
