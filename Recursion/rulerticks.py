#draws a ruler recursively 

def draw_ruler(inches, major_length): #expects major_length >= 2
    '''draws ruler w/ given number of inches and tick length for major ticks (whole inches)'''
    draw_line(major_length) #0 inch line
    for j in range(1, inches + 1):
        draw_interval(major_length-1) #draws interval from j-1 to j inches
        draw_line(major_length)


def draw_line(length):
    '''draws line with length # of ticks with optional number label at end'''
    print('-' * length)

def draw_interval(center_length): #makes recursive calls
    '''draws interval based on given center_length'''
    if center_length == 1:
        draw_line(1)
    else:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)
