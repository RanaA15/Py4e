#Rewrite your pay computation to give the employee 1.5 times 
#the hourly rate for hours worked above 40 hours. 
#This time, utilize the try and except so that the program handles
#non-numeric input gracefully by printing a message and 
#exiting the program
hours = input('Enter Hours: ')
try:
    hours = float(hours)
except: 
    print("Error, please enter numeric input")
    quit()
rate = input('Enter Rate: ')
try:
    rate = float(rate)
except: 
    print("Error, please enter numeric input")
    quit()
    
if hours > 40:
    opay = (hours - 40) * (rate * 1.5)
    pay = (40 * rate) + opay
else:
    pay = hours * rate
print('Pay: ', pay)


