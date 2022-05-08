
fname = open('romeo.txt')
things = list()
for line in fname:
    words = line.split()
    for word in words:
        if word not in things:
            things.append(word)
        else: continue
things.sort()
print(things)
