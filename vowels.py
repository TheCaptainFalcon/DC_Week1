vowels = "aeiou"
user = input("Enter: ")
new_string = " "

for i in range(len(user)):
    if user[i] == user[i-1] and user[i] in vowels:
        new_string += user[i] * 4
    else:
        new_string += user[i]
print(new_string)

#while loop version
#while i < len(user)
# i += 1