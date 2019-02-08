i_m = 0.1 # inter module

size('A3')

p_shape = 0.4

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


path = u'orange-horizontal.pdf'
img_w, img_h = imageSize(path)


scaling_x = (w * (1+p_shape/2))/img_w
scaling_y = w*p_shape / img_h

for x in range(_w):
    for y in range(_h):
        square = False
        if (y % 2 == x % 2 == 0) or (y % 2 == x % 2 == 1):
            square = True

        if x < _w - 1:
            with savedState():
                scale(x=scaling_x, y=scaling_y)
                s_x = (x * w + i_m * w) / scaling_x
                s_y = (y * h + i_m * w) / scaling_y
                image(path, (s_x, s_y))
                            
        if square:
            d_square(x,y)
        else:
            d_circle(x,y)
            
            