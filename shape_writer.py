from random import choice

i_m = 0.2 # inter module

colors = {
    "yellow": {
            "rgb": (247/255, 199/255, 31/255),
            "cmyk": (247/255, 199/255, 31/255)
        },
    "orange": {
            "rgb": (255/255, 92/255, 0/255),
            "cmyk": (0, 0.68, 1, 0)
        },
    "white": {
            "rgb": (255/255, 255/255, 255/255),
            "cmyk": (0, 0, 0, 0)
        },
    "black": {
            "rgb": (0/255, 0/255, 0/255),
            "cmyk": (0, 0, 0, 1)
        }
    }
    
bg_color = colors["yellow"]
c1 = colors["white"]
c2 = colors["black"]

# yellow (shapes)
color1_cmyk = c1["cmyk"]
color1_rgb = c1["rgb"]

# orange (connections)
color2_cmyk = c2["cmyk"]
color2_rgb = c2["rgb"]

cmyk_mode = False
img_mode = 'png'
alpha = 1

p_h = 1 - 0.4
p_d = 1 - 0.2

# size('A3')

# size(1280, 320)
# _w = 24 # n columns

size(750, 870)
_w = 7 # n columns

_h = int(height()/width() * _w)
w = width()/_w
h = height()/_h

if cmyk_mode:
    cmykFill(*bg_color["cmyk"])
else:
    fill(*bg_color["rgb"])
    
rect(0,0, width(), height())

p_shape = 0.37


# centers shapes
shift_x = (w * (1 - p_shape)) / 2 - w * i_m
shift_y = (h * (1 - p_shape)) / 2 - h * i_m
translate(shift_x, shift_y)

def d_circle(x,y):
    oval(0, 0, actual_width, actual_width)
    
def d_square(x,y):
    rect(0, 0, actual_width, actual_width)

def create_color_map(color):
    gm = ImageObject()
    with gm:
        size(1,1)
        if cmyk_mode:
            cmykFill(*color)
        else:
            fill(*color)
        rect(0,0, 1,1)
    return gm


diag = sqrt((w * (1 - i_m))**2 + (h * (1 - i_m))**2)
actual_width = w * p_shape
inter_column = w * i_m


# draws connections...
for x in range(_w):
    for y in range(_h):
        
        with savedState():

            translate(x * w + inter_column, y * h + inter_column)

            # horizontal & vertical connections
            if x < _w - 1 and y < _h - 1 and random() > p_h:
                with savedState():
                    
                    # chooses image
                    path_h = 'connections/' + img_mode + '/' + choice([
                        'ort_0',
                        'ort_1',
                        'ort_2',
                        'ort_3',
                        'ort_4',
                        'ort_5',
                        'ort_6',
                        'ort_7',
                        'ort_8',
                        'ort_9']) + '.' + img_mode
                    img_w, img_h = imageSize(path_h)
                    
                    scaling_x_h = w/img_w
                    scaling_y_h = w*p_shape / img_h

                    if cmyk_mode:
                        gm = create_color_map(color2_cmyk)
                    else:
                        gm = create_color_map(color2_rgb)
                    
                    r = random()
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
                        
                    im = ImageObject(path_h)
                    im.colorMap(gm)
                    image(im, (0, 0))


            #diagonal connections
            if x < _w - 1 and y < _h - 1 and random() > p_d:
            # if x == 2 and y == 2:
                with savedState():

                    # chooses image                                        
                    path_d = 'connections/' + img_mode + '/' + choice([
                        'diag_1',
                        'diag_2',
                        'diag_3',
                        'diag_4',
                        'diag_5']) + '.' + img_mode
                        
                    img_w, img_h = imageSize(path_d)
                    scaling_x_d = diag/img_w
                    scaling_y_d = scaling_x_d
                    
                    if cmyk_mode:
                        gm = create_color_map(color2_cmyk)
                    else:
                        gm = create_color_map(color2_rgb)
                    
                    if x > 0 and y > 0 and random() > 0.5:
                        scale(x=-scaling_x_d, y=scaling_y_d)
                        translate(-w*p_shape / scaling_x_d, 0)
                    else:
                        scale(x=scaling_x_d, y=scaling_y_d)
                        
                    offset_x = (w * p_shape/4) / scaling_x_d
                    offset_y = (h * p_shape/4) / scaling_y_d
                    translate(offset_x, offset_y)
                    im = ImageObject(path_d)
                    im.colorMap(gm)
                    image(im, (0, 0))



# overlays connections with shapes
if cmyk_mode:
    cmykFill(*color1_cmyk, alpha) 
else:
    fill(*color1_rgb, alpha)

for x in range(_w):
    for y in range(_h):
        square = False
        if (y % 2 == x % 2 == 0) or (y % 2 == x % 2 == 1):
            square = True 
                   
        with savedState():
            
            translate(x * w + inter_column, y * h + inter_column)
            if square:
                d_square(x,y)
            else:
                d_circle(x,y)
            
            