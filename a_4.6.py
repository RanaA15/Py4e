#Rewrite your pay computation with time and a half (1.5x) for overtime
# and create a function called computepay which takes two paramters (hours and rate)

hours = input('Enter hours:')
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
def computepay(hours, rate):
    if hours > 40:
        opay = (hours - 40) * (rate * 1.5)
        pay = (40 * rate) + opay
    else:
        pay = hours * rate
    print ('Pay:', pay)

computepay(hours, rate)

