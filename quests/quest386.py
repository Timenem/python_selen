def checkio(opacity):
    a, b = 1, 1
    age = 0
    while opacity != 10000:
        age += 1
        if age == b:
            opacity += b
            a, b = b, a+b
        else:
            opacity -= 1
    return age
