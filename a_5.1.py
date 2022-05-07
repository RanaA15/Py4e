#Write a program which repeatedly reads numbers unntil the user enters "done". 
#Once "Done" is entered, print out the total, count and average of the numbers.
# If the user enters anything other thana  number, detect their mistake using try and except
#and print an error message and skip to the next number
num = 0
total = 0.0
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
  
print(total, num, total/num)