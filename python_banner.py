# string = input("Enter a string: ")

# print ("*") * (len(string)+6)
# print ("*  ") + string +  (" *")
# print ("*") * (len(string)+6)

string = input('Enter any string: ')
add_string = (len(string) + 6)
print ('*') + add_string

print ('*  ') + string + ('  *')
print ('*') + len(string)+6