def rgb_to_grayscale(color:str):
    r = 0.299 * int(color[1:3], 16)
    g = 0.587 * int(color[3:5], 16)
    b = 0.114 * int(color[5:], 16)
    gray = round(r + g + b)
    return "#{:02X}{:02X}{:02X}".format(gray, gray, gray)
