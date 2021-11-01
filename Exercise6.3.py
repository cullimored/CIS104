def count(word, letter):
    counter = 0

    for character in word:
        if character == letter:
            counter = counter+ 1
    print(counter)

word = input('Enter the word: ')
letter = input('Enter the letter: ')
count(word ,letter)
