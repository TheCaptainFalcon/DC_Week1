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
