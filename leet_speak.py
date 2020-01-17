#prompt for string that will convert to leet
leet = input("Please enter a string that will print it into leet ")

#convert string into upper

leet_list = {"A" : "4" , "E" : "3" , "G" : "6" , "I" : "1" , "O" : "0" , "S" : "5" , "T" : "7"}
print(leet.replace("x" , "y"))




#create a legend that treats capitalized letters as leet counterpart



#if else statement to convert

string =input("string to translate to leetspeak: ").upper()
index = 0
while index < len(string):
    if string[index] == "A":
        print("4", end= "")
index += 1

#2 method
letters_to_replace ="AEGIOS"
leet_numbers = "4361057"
translation = ""

for i in[range(len(string))]:
    add_to = ""
    for j in range(len(letters_to_replace)):
        if string[i] == letters_to_replace[j]:
                add_to = str(leet_numbers[j])
                break
            else:
                add_to = string[i]
        translation += add_to
print(translation)

