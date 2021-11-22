addresses = dict()
fname = input('Enter file name: ')
try:
    fhan = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()
for line in fhan:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in addresses:
            addresses[words[1]] = 1
        else:
            addresses[words[1]] = addresses[words[1]] + 1
print(addresses)
