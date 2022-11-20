def parse(data):
    '''Returns a list according to the data input'''
    counter = 0
    output_array = []
    for letter in data:
        if letter == 'i':
            counter += 1
        elif letter == 'd':
            counter -= 1
        elif letter == 's':
            counter *= counter
        elif letter == 'o':
            output_array.append(counter)
    return output_array
