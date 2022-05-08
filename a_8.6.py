#Rewrite the program that prompts the user for a list of numbers and prints out
#the maximum and minimum of the numbers at the end when the user enters "done". Write
# the program to store the numbers the user enters in a list and use the max()
# and min() functions to compute the maximum and minimum numbers after the loop completes


things = list()
while True:
    x = input('Enter a number: ')
    if x == 'done': break
    try: 
        num = float(x)
        things.append(num)
    except:
        print('Invalid number')
        continue
print('Maximum: ', max(things))
print('Minimum: ', min(things))