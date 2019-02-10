from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

# -1 slope
draw_line(250, 0, 0, 250, screen, [255,0,0])
# 1 slope
draw_line(250, 250, 500, 0, screen, [255,0,0])

# 0 slope
draw_line(0, 250, 500, 250, screen, [0,0,255])
# undefined slope
draw_line(250, 500, 250, 0, screen, [0,0,255])

draw_line(100, 100, 200, 0, screen, color)
draw_line(250, 250, 500, 230, screen, color)
draw_line(250, 250, 300, 0, screen, color)


'''
x0 = 0
y0 = 0
x1 = 0
y1 = YRES
x2 = XRES
y2 = YRES
x3 = XRES
y3 = 0
i = 0
diffa = 10
diffb = 6
while (i < 100) :
    draw_line(x0, y0, x1, y1, screen, [255-x0/2, 255-y0/2, x0+y0/4])
    draw_line(x1, y1, x2, y2, screen, [255-x1/2, 255-y1/2, x1+y1/4])
    draw_line(x2, y2, x3, y3, screen, [255-x2/2, 255-y2/2, x2+y2/4])
    draw_line(x3, y3, x0, y0, screen, [255-x3/2, 255-y3/2, x1+y3/4])
    x0 += diffa
    y0 += diffb
    x1 += diffb
    y1 -= diffa
    x2 -= diffa
    y2 -= diffb
    x3 -= diffb
    y3 += diffa
    i += 1
    if (i % 8 == 0):
        diffa -= 1
        diffb -= 1
'''

display(screen)
save_extension(screen, 'img.png')
print("img.png")

def draw_square(x0, y0, x1, y1, len, color):
    A = y1 - y0
    B = x1 - x0
    draw_line(x0, y0, x1, y1, screen, color)
    draw_line

    return
