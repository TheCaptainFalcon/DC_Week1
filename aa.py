string =input("string to translate to leetspeak: ").upper()
index = 0
while index < len(string):
    if string[index] == "A":
        print("4", end= "")
    elif string[index] == "E":
        print("3", end= "")
index += 1
