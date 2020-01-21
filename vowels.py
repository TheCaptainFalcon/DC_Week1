vowels = "aeiou"

#empty string to add input and conversion into
empty_string = " "

#prompt
con = input("Enter: ")

#if vowel -1 gives same as if vowel exists, condition is met
for j in range(len(con)):
    if con[j] == con[j-1] and con[j] in vowels:
        empty_string += con[j] * 4
    else:
        empty_string += con[j]
print(empty_string)