#make 2 different lists of the same length
list_one = [10, 20, 30]
list_two = [1, 5, 10]

#zip is like setting a pattern for set length vectors
#adds corresponding position between the lists
convert =[list_one + list_two for list_one, list_two in zip(list_one, list_two)]

#return results
print(convert)

#2-dimensional version#

#make a 2-dim/nested? list of same length
list1 = [ [10, 20, 30], [1, 5, 10] ]
#
[(sum(x)for x in zip(*list1))]
print(list1)

##go back to this and figure out