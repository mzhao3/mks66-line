from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x1<x0:
        x0,x1=x1,x0
        y0,y1=y1,y0
        
    x = x0
    y = y0

    A = y1 - y0
    B = x0 - x1

    # octant 1
    if (A <= (-1 * B) and A >= 0):
        D = 2*A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (D > 0):
                y += 1
                D += 2*B
            x += 1
            D += 2*A

    # octant 2
    elif (A > (-1 * B) and B <= 0 ):
        D = A + 2 * B
        while (y <= y1):
            plot(screen, color, x, y)
            if (D < 0):
                x += 1
                D += 2*A
            y += 1
            D += 2*B

    # octant 7
    if (A < 0):
        #print("the difference in y:" + str(A))
        #print("the difference in x:" + str(B))
        if (A < B):
            #print("in octant 7")
            D = A + 2 * B
            while (y >= y1):
                #print(y)
                plot(screen, color, x, y)
                if (D > 0):
                    x += 1
                    D += 2*A
                y -= 1
                D += -2*B


        #fix
        elif ((-1 * A) <= (-1 * B)):
            #print("in octant 8")
            D = -2*A + B
            while (x <= x1):
                plot(screen, color, x, y)
                if (D > 0):
                    y -= 1
                    D += 2*B
                x += 1
                D += -2*A

    return
