name = str.upper(input("What is your name?"))
name_count = len(name)

greeting = "Hello, " + str(name) + "!"
greeting_cap = greeting.upper()

str_name_count = "Your name has " + str(name_count) + " Letters in it! Awesome!"
str_name_count_cap = str_name_count.upper()

print(greeting_cap)
print(str_name_count_cap)
