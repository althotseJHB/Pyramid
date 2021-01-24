# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():

    while(True):
        shape =  str(input("Shape?: "))
        shape = shape.lower()
        if shape == "pyramid" or shape == "square" or shape == "triangle" or shape == "diamond" or shape == "kite" or shape == "parallelogram" or shape == "rectangle":
            return shape
        break
        # else:
        #     return get_shape()
    return get_shape()



# TODO: Step 1 - get height (it must be int!)
def get_height():
    # while (True):
        # height = input("Height?: ")
        # height = height.isdigit()0
        # if height <= 80:
        #     return height
        # else:
        #     return get_height()
        try:
            height = int(input("Height?: "))
            if height <= 80:
                return height
        except:
            return get_height()




# TODO: Step 2
def draw_pyramid(height,outline):
    if outline is False:
        i = height - 1
        for j in range(1,height*2,2):
            print(" "*i+j * "*")
            i-=1

    elif outline:
        i = 0
        j = 1
        height -= 2
        h = height
        print(" "*(height+1)+ "*") #print 9 spaces with a star at the end {height -= 2}
        while height > 0: #print spaces outside, then to print the inner spaces with a star
            print(" "*(height)+"*"+" "*j+"*")
            i += 1
            j += 2
            height -= 1
        if height == 0:
            print("*"*(h*2+3))

# TODO: Step 3
def draw_square(height, outline):

    if outline is False:
        for i in range(height):
            print("*"*height)


    elif outline:
        print("*"* height)
        for i in range(height-2):
            print("*" + " "*(height-2) + "*")
        print("*"* height)


    # elif outline:
    #     space = 0
    #     print("*"* height)
    #     for i in range(height-2):
    #         print(' ' * space + "*" + " "*(height-2) + "*")
    #         space += 1
    #     print("*"* height)
# TODO: Step 4
def draw_triangle(height, outline):

    if outline is False:
        for i in range(1,height+1):
            print("*"*i)

    elif outline:
        print("*")
        for i in range(1,height-1):
            print("*"+" "*(i-1)+"*")
        print("*"* height)

# def draw_kite(height, outline):
#
#     if outline is False:
#         for i in range(1,height+1):
#             # top = 1
#             print(" " * (height-i) + "*" * (i*2))
#             # top = 2
#         for a in range(height-1,0,-2):
#             # bottom = 2
#             print(" " * (height-a)+"*"* (a*2))
#             # bottom = 1
#
#     elif outline:
#         for i in range(1,height+1):
#             print(" " *(height-i) + "*" *(2*i-1))
#             i = 0
#             j = 1
#             height -= 2
#             h = height
#             while height > 0:
#                 print(" "*(height)+"*"+" "*j+"*")
#                 i += 1
#                 j += 2
#                 height -= 1
            # if height == 0:
            #     print("*"*(h*2+3))

def  draw_rectangle(height,outline):


    if outline is False:
        width = height * 2
        for rect in range(height):
            print("*"*width)

    elif outline:
        width = height * 2
        print("*"* width)
        for i in range(height-2):
            print("*" + " "*(width-2) + "*")
        print("*"* width)


def draw_diamond(height, outline):

    if outline is False:
        i = height - 1
        for i in range(1,height+1,2):
            print(" "*(height-i+1)+"* "*i)
        for i in range(height+1,0,-2):
            print(" "*(height-i+1)+"* "*i)

    elif outline :

        i = height - 1
        # print(" "*(height-i+1)+"*")
        for i in range(1,height+1,2):
            if i == 1:
                a = 0
            else:
                a = 1
            print(" "*(height-i+1)+"* "+"  "*(i-2)+"* "*a)
        for i in range(height+1,0,-2):
            if i == 1:
                a = 0
            else:
                a = 1
            print(" "*(height-i+1)+"* "+"  "*(i-2)+"* "*a)



def draw_parallelogram(height, outline):

    if outline is False:
        i = height - 1
        for j in range(height,0,-1):
            print(" "*(height-j+1)+"*"*i)

    else:
        space = 0
        stars = height
        for x in range(height):
            if x == 1:
                print('*' * stars)
            if x > 1 and x < height:
                print(' ' * space + '*' + ' '  * (stars) + '*')
            if x == height + 9 :
                print('*' * stars)
            space += 1

    #elif outline:
    #    i = height - 1
    #    for j in range(height,0,-1):
    #        print(" "*(height-j+1)+" "*(i)+"*")





# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height,outline)
    elif shape == "kite":
        draw_kite(height, outline)
    elif shape == "diamond":
        draw_diamond(height, outline)
    elif shape == "parallelogram":
        draw_parallelogram(height, outline)
    elif shape == "rectangle":
        draw_rectangle(heidef run_game(): from user to draw outline or solid
def get_outline():
    outline = input("Outline:Y/N?: ")
    if outline.lower() == "y":
        return True
    if outline.lower() == "n":
        return False
    # return False
    return get_outline()


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)
