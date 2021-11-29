hours = dict()
lst = list()
fnam = input('Enter file name: ')
try:
    fhan = open(fnam)
except FileNotFoundError:
    print('File cannot be opened:', fnam)
    quit()
for line in fhan:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    pos = words[5].find(':')
    hour = words[5][:pos]
    if hour not in hours:
       hours[hour] = 1
    else:
        hours[hour] += 1
for key, val in list(hours.items()):
    lst.append((key, val))
lst.sort()
for key, val in lst:
    print(key, val)
