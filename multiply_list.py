#list of nums
old_list = [1, 2, 3, 4, 5]

#factor to multiply
mult = 10

#new list
new_list = []

#select each number in list to * mult -> append to new_list -> print
for x in old_list :
    new_list.append(x * mult)
    print(new_list)