#prompt for how many coins you want
#import math library for infinite use
import math
x = 0

print("You have 0 coins. ")

#ask if them want another - loop it so it continually asks until reject (break)
accept = input("Do you want another? ")

#infinite used to disable number loop limitation
while x < float(math.inf):
    if accept == "yes" :
        x += 1
        #new var for input must be created otherwise it will be reliant on line 8
        #line 8 input is only good for initial yes or no - not future actions
        accept2 = input("You have " + "%s" %x + " coins. " + "Do you want another? ")
        if accept2 == "no":
            break
    elif accept == "no": 
        break

