#prompt for string 
word = input("Enter a word ")
counter = {}

#dict.get with value of starting 0
#linked to x[dict] to narrow letters
#count each occurrence of letter 
for letter in word:
    counter[letter] = counter.get(letter, 0) + 1
    print(str(counter))

for letter in word:
    counter[letter] = counter.get(letter, 0)
    print(counter)