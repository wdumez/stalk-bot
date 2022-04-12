
from tkinter import W

from matplotlib.style import available

def unpack(rects):
    middle = 0
    rects_not_empty = 0
    try:
        for column, row, width, height in rects:
            print(column, width)
            middle = column + (width/2)
            rects_not_empty = 1
    except:
        print("ween")
        
    return middle, rects_not_empty



def MainController(image_width, rects_faces, rects_full_body, rects_upper_body, rects_lower_body): 
    
    middle_screen = image_width/2
    window = (middle_screen - 20, middle_screen + 21)

    #unpack the rects received: rects_full_body_not_empty=1 of not empty
    middle_full_body, rects_full_body_not_empty = unpack(rects_full_body)
    middle_upper_body, rects_upper_body_not_empty = unpack(rects_upper_body)
    middle_lower_body, rects_lower_body_not_empty = unpack(rects_lower_body)

    #voor debuggen
    #rects_faces = []
    
    try:
        average_middle = (middle_full_body + middle_upper_body + middle_lower_body)/(rects_full_body_not_empty + rects_upper_body_not_empty + rects_lower_body_not_empty)
        print(f"avarge middle: {average_middle}") 
    except:
        print("alles leeg")

    if((rects_full_body_not_empty or rects_upper_body_not_empty or rects_lower_body_not_empty) and len(rects_faces) == 0):
        if(average_middle > window[1]):
            return "Links wiel draaien"
        if(average_middle < window[0]):
            return "Rechts wiel draaien"
        return "Vooruit" 
    if(not(rects_full_body_not_empty or rects_full_body_not_empty or rects_full_body_not_empty) and len(rects_faces) == 0):    
        return "Links of Rechts draaien (zoeken)"
          
    return "Stoppen"    




