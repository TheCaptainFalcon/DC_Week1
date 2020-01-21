#prompt for string - uppercase
leet = input("Enter a string to convert into leet ").upper()
for conv in leet:
    if conv == "A":
        leet = leet.replace("A","4")
    elif conv == "E":
        leet = leet.replace("E","3")
    elif conv == "G":
        leet = leet.replace("G","6")
    elif conv == "I":
        leet = leet.replace("I","1")
    elif conv == "O":
        leet = leet.replace("O","0")
    elif conv == "S":
        leet = leet.replace("S","5")
    elif conv == "T":
        leet = leet.replace("T","7")
print(leet)        


#Method 2 (key:point dictionary) - (needs working)
# leet = input("Enter a string ").upper()
# key = {"A":"4", "E":"3", "G":"6", "I":"1", "O":"0", "S":"5", "T":"7"}
# empty_string = " "

# for convert in leet:
#     if convert in key:
#         empty_string += key[convert]
#     elif convert not in key:
#         empty_string += leet[convert]
#         pass    
# print(empty_string)