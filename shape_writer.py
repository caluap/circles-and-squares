i_m = 0.1 # inter module

size('A3')

p_shape = 0.5

_w = 10
_h = 14
w = width()/_w
h = height()/_h

def d_circle(x,y):
    fill(0)
    actual_width = w * p_shape
    inter_column = w * i_m
    oval(x * w + inter_column, y * h + inter_column, actual_width, actual_width)
    
def d_square(x,y):
    fill(194/255, 181/255, 155/255)
    actual_width = w * p_shape
    inter_column = w * i_m
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
            
            