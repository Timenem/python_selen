
"""
Write an algorithm that takes an array and moves 
all of the zeros to the end, preserving the order of the other
elements.
"""
# first variant 
def move_zeros(array):
    for i in array:
        if i ==0:
            array.remove(i)
            array.append(i)
    print(array)
    
# second variant 
def move_zeros_to_end(array):
    zero_str = '0'
    zeros_counter = array.count(0)
    for i in array:
        if i ==0:
            array.remove(i)
    zeros_array =str(zero_str).split()*zeros_counter
    array = (array+(list(map(int,zeros_array))))
    print(array)
    
