#Prompt the user for a number
#compare that number to a pre-defined value
#if the numbers match, tell the user they are a mind reader
#if they dont match, tell the user thanks for playing

user_input = int(input("What number am I thinking of? "))

#Constant
MAGICNUMBER = 9

if user_input == MAGICNUMBER:
    print("CAN YOU READ MINDSSS?")

else: 
    print("That's not correct")
