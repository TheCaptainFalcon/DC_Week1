#make 2 different lists of the same length
list_one = [10, 20, 30]
list_two = [1, 5, 10]

#zip is like setting a pattern for set length vectors
#multiplies corresponding position between the lists
convert =[list_one * list_two for list_one, list_two in zip(list_one, list_two)]

#return results
print(convert)