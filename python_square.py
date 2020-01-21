#print a 5x5 square of * numbers
#instead of flat print - make them stacked

import numpy

#arange - returns an array with evenly spaced elements per the interval
#formatted like (start, stop, step(optional))
#reshape - row, columns
array1 = numpy.arange (0,25).reshape(5,5)
print (array1)

#scenario 2


#print a 5x5 square of * characters
#instead of flat print - make them stacked
#repeat ("<whatever>", <how many times>)
array2 = numpy.repeat(["*"], 25).reshape(5,5)
print (array2)


#Scenario 3 - using a loop instead of numpy
#total characters are given 25 -- 5x5

