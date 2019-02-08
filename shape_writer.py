i_m = 81 # inter module

shape_size = 584

p_shape = 584/1832 # proportion of shape in each module
p_i = 80/1832 # x proportion of intercolumn in each module        

circles = ['a','c','e']
squares = ['b','d','f']

big_block = (i_m + 1753, i_m + 1753 + i_m)
small_block = (i_m + 1753, i_m + shape_size + i_m)

size('A3')

_w = 10
_h = 14
w = width()/_w
h = height()/_h

def d_circle(x,y):
    fill(0)
    actual_width = w * p_shape
    inter_column = w * p_i
    oval(x * w + inter_column, y * h + inter_column, actual_width, actual_width)
    
def d_square(x,y):
    fill(194/255, 181/255, 155/255)
    actual_width = w * p_shape
    inter_column = w * p_i
    rect(x * w + inter_column, y * h + inter_column, actual_width, actual_width)



for x in range(_w):
    for y in range(_h):
        square = False
        if y % 2 == 0:
            if x % 2 == 0:
                square = True
        if y % 2 == 1:
            if x % 2 == 1:
                square = True
                
        if square:
            d_square(x,y)
        else:
            d_circle(x,y)
            
            