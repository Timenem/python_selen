"""
Description:

Write a function with the signature shown below:

def is_int_array(arr):
    return True

    returns true  / True if every element in an array is an integer or a float with no decimals.
    returns true  / True if array is empty.
    returns false / False for every other input.


"""
def is_int_array(a):
    return isinstance(a, list) and all(isinstance(x, (int, float)) and x == int(x) for x in a)
