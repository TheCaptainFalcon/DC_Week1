#use list containing numbers/strings 
#add in some duplicates + some in different places (not next to each other)
list1 = [1, 1, 2, 1, 2, 5, 10, 2, 25, 50, 5, 100]

#create another list 
# make it so that it has the same contents of first list
#while removing any duplicates
list2 = []

for x in list1 :
    #repeat - if the same vars in list1 are not in list2 - adds them
    #essentially looks at list2 and compares to list 1
    if x not in list2 :
        list2.append(x)

#repeat - specifies the items of var x in list2 to be printed
for x in list2 :
    print(x)