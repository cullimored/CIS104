dictaddresses = dict()
maximum = 0
maxaddress = ''



fname = input('Enter file name: ')
try:
    fhan = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhan:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    if words[1] not in dictaddresses:
        dictaddresses[words[1]] = 1
    else:
        dictaddresses[words[1]] += 1

for address in dictaddresses:
    if dictaddresses[address] > maximum:
        maximum = dictaddresses[address]
        maxaddress = address

print(maxaddress, maximum)
