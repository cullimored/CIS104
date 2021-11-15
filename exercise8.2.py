fname = open('exercise8_2.txt')
for line in fname:
    words = line.split()

    if len(words) <3:
        continue
    if words[0] if not 'From':
        continue
    print(words[2])
