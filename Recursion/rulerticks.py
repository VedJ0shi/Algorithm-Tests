#draws a ruler recursively 

def draw_ruler(inches, major_length): #expects major_length >= 2
    '''draws ruler w/ given number of inches and length of major ticks (indicate whole inches)'''
    draw_line(major_length) #at 0 inch mark
    for j in range(1, inches + 1):
        draw_interval(major_length-1) #fills the interval between j-1 and j inches
        draw_line(major_length) #draws major tick for jth inch mark


def draw_line(length):
    '''draws line with length # of dashes with optional number label at end'''
    print('-' * length)

def draw_interval(center_length): #makes recursive calls
    '''draws interval based on given center_length'''
    if center_length == 1:
        draw_line(1)
    else:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)
