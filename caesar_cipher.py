#ROT13
caesar = "lbh zhfg hayrnea jung lbh unir yrnearq"
key = {"a":"n", "b":"o", "c":"p", "d":"q", "e":"r", "f":"s", "g":"t", "h":"u", "i":"v", "j":"w", "k":"x", "l":"y", "m":"z", "n":"a", "o":"b", "p":"c", "q":"d", "r":"e", "s":"f", "t":"g", "u":"h", "v":"i", "w":"j", "x":"k", "y":"l", "z":"m"}
string = " "

#if within key, replaces and adds conversion into string
for cipher in caesar:
    if cipher in key:
        string = string + key[cipher]
        print (string)
    elif cipher not in key:
        string += " "
