#Take the following python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after 
# the colon character and then use the float function to convert the extracted string
# into a floating point number

str = 'X-DSPAM-Confidence: 0.8475'

index = str.find(':')
print(index)
num = float(str[index+1:])
print(num)