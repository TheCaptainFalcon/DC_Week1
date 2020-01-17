#make 2 separate pairs of lists with the same length
list1a = [10, 20, 30]
list1b = [1, 5, 10]

list2a = [2, 4, 6, 8, 10]
list2b = [10, 10, 10, 10, 10]

#zip is like setting a pattern for set length vectors
#adds corresponding position between the lists
convert =[list1a + list1b for list1a, list1b in zip(list1a, list1b)]
convert2 = [list2a + list2b for list2a, list2b in zip(list2a, list2b)]

#return results
print(convert)
print(convert2)

#2-dimensional version

#make a two 2-dim/nested? list of same length
list1 = [ [[10, 20, 30], [1, 5, 10]] , [[[2, 4, 6, 8, 10] , [10, 10, 10, 10, 10]] ]

#solve this after 1st addition