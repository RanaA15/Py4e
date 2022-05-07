#Write antohoer program that prompts for a list of numbers as above
#and at the end prints out both the maximum and minimum of the numbers instead of the average

num = 0
total = 0.0
largest = None
smallest = None

while True :
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
        num = num + 1
        total = total + fval
    except: 
        print('Invalid input')
        continue
    if largest is None:
        largest = fval
    if smallest is None: 
        smallest = fval
    elif largest < fval:
        largest = fval
    elif smallest > fval:
        smallest = fval
  
print('Total:',total, 'Count:', num, 'Largest number:', largest,'Smallest number:', smallest)