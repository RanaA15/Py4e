#Rewrite your pay computation to give the employee 1.5 times 
# the hourly rate for hours worked above 40 hours. 
hours = input('Enter Hours: ')
hours = float(hours)
rate =  input('Enter Rate: ')
rate = float(rate)
if hours > 40:
    opay = (hours - 40) * (rate * 1.5)
    pay = (40 * rate) + opay
else:
    pay = hours * rate
print('Pay: ', pay)

