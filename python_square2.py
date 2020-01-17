import numpy

#prompt for var N - equally stacked array
#N -> (row * column)
N = int(input("How big is the square?"))

array1 = numpy.repeat(["*"], N).reshape(N, N)
print(str(array1))