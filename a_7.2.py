fname = input('Enter a file name: ')
count = 0
tnum = 0
try:
    fhand = open(fname)
except:
    print('File cannot be opened')
    quit()
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos = line.find(':')
        num = float(line[pos+1:])
        tnum = tnum + num
print('Average spam confidence:', tnum/count)