import numpy

#prompt input for width and height
width = int(input("Enter the width. "))
height = int(input("Enter the height. "))

#multiply input to convert into full amount
full_dimension = (width * height)

#use reshape to break down
box_combined = numpy.repeat("*", full_dimension)
box_shape = box_combined.reshape (height, width)

#select index of nested index
n-1 and index[1]
#between those two values -> replace into a space of void?
#select the nested index to replace with same width value ->
#n-1 and between index[1] -- these are the specified range
bot_box = (width-1)
in_box = [1:bot_box]
inner_box = in_box[1:width-1]

print(box_shape)

## needs reworking