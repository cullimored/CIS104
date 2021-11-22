domnam = dict()                     
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
    else:
        atpos = words[1].find('@')
        domain = words[1][atpos+1:]
        if domain not in domnam:
            domnam[domain] = 1
        else:
            domnam[domain] = domnam[domain] + 1
print(domnam)
