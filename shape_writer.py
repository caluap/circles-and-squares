i_m = 0.1 # inter module

p_h = 0.8
p_d = 0.9

alpha = 1

size('A3')

p_shape = 0.35

_w = 10
_h = 14
w = width()/_w
h = height()/_h

def d_circle(x,y):
    oval(0, 0, actual_width, actual_width)
    
def d_square(x,y):
    rect(0, 0, actual_width, actual_width)


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

        with savedState():
            
            actual_width = w * p_shape
            inter_column = w * i_m
            translate(x * w + inter_column, y * h + inter_column)

            # horizontal & vertical connections
            if x < _w - 1 and random() > p_h:
                with savedState():
                    r = random()
                    print(r)
                    # horizontal
                    if r > 0.5:
                        scale(x=scaling_x_h, y=scaling_y_h)
                        offset_x = (w * p_shape/2) / scaling_x_h
                        translate(offset_x, 0)
                    else: #vertical
                        scale(x=scaling_y_h, y=scaling_x_h)
                        rotate(90)
                        offset_x = (w * p_shape / 2) / scaling_x_h
                        offset_y = -(h * p_shape) / scaling_y_h
                        translate(offset_x, offset_y)
                        
                    image(path_h, (0, 0))


            #vertical connections
            if x < _w - 1 and y < _h - 1 and random() > p_d:
                with savedState():
                    scale(x=scaling_x_d, y=scaling_y_d)
                    offset_x = (w * p_shape/4) / scaling_x_d
                    offset_y = (h * p_shape/4) / scaling_y_d
                    translate(offset_x, offset_y)
                    image(path_d, (0, 0))
               
            fill(0, alpha)            
            if square:
                d_square(x,y)
            else:
                d_circle(x,y)
            
            