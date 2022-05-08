fname = input('Enter a file name: ')
words = list()
count = 0
try:
    fhand = open(fname)
except:
    print('File cannot be opened')
    quit()

for line in fhand:
    if not line.startswith('From '):
        continue
    if line.startswith('From '):
        count = count + 1
        words = line.split()
        print(words[1])
print('There were', count,'lines in the file with From as the first word')