import numpy
import math

#prompt for var N - equally stacked array
#N -> (row * column)
n = int(input("How big is the square? "))

#user input * itself
n_ex = math.pow(n,2)

#in order to maintain type balance...
#* is contant and must be a string
#var N must be an integer
array1 = numpy.repeat("*", n_ex)
array2 = array1.reshape(n,n)
print(array2)

#if you can do n^2 of repeat, it could solve the reshape issue
#ie. user input = 7 -> 49 .shape(7,7)
