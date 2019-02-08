i_m = 0.1 # inter module

p_h = p_d = 0.9

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
    fill(0)
    actual_width = w * p_shape
    inter_column = w * i_m
    rect(x * w + inter_column, y * h + inter_column, actual_width, actual_width)


path_h = u'orange-horizontal.pdf'
path_d = u'purple-diagonal.pdf'

img_w, img_h = imageSize(path_h)

scaling_x_h = w/img_w
scaling_y_h = w*p_shape / img_h

img_w, img_h = imageSize(path_d)
diag = sqrt((w * (1 - i_m))**2 + (h * (1 - i_m))**2)
scaling_x_d = diag/img_w
scaling_y_d = scaling_x_d

for x in range(_w):
    for y in range(_h):
        square = False
        if (y % 2 == x % 2 == 0) or (y % 2 == x % 2 == 1):
            square = True

        # horizontal connections
        if x < _w - 1 and random() > p_h:
            with savedState():
                scale(x=scaling_x_h, y=scaling_y_h)
                s_x = (x * w + i_m * w + w * p_shape/2) / scaling_x_h
                s_y = (y * h + i_m * w) / scaling_y_h
                image(path_h, (s_x, s_y))

        #vertical connections
        if x < _w - 1 and y < _h - 1 and random() > p_d:
            with savedState():
                scale(x=scaling_x_d, y=scaling_y_d)
                s_x = (x * w + i_m * w + w * p_shape/4) / scaling_x_d
                s_y = (y * h + i_m * w + h * p_shape/4) / scaling_y_d
                image(path_d, (s_x, s_y))
            
                                        
        if square:
            d_square(x,y)
        else:
            d_circle(x,y)
            
            