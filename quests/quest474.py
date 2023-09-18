def align_right(text,width):
    words = text.split(" ")
    lines = []
    length = 0
    line = []
    for word in words:
        if length + len(word) <= width:
            length += len(word) + 1
            line.append(word)
        else:
            lines.append("{:>{}}".format(" ".join(line), width))
            line = [word]
            length = len(word) + 1
            
    lines.append("{:>{}}".format(" ".join(line), width))
    
    return "\n".join(lines)
