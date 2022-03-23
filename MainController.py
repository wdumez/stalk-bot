def determine_action(rects_faces, rects_full_body, rects_upper_body, rects_lower_body):
    action="Niks"
    if (len(rects_full_body) == 0 and len(rects_faces) == 0 and len(rects_upper_body) == 0):
        action="Zoeken"
    if ((len(rects_full_body) != 0 or len(rects_upper_body) != 0) and len(rects_faces) == 0):
        action="Rijden"
    if (len(rects_faces) != 0):
        action="Stoppen"

    return action