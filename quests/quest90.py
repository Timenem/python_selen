"""
 We have a List of booleans. Let's check if the majority of elements are true. 
"""

def is_majority(items: list) -> bool:
    if len(items) == 0 :
        return False
    elif sum(list(items)) > list(items).count(False):
        return True
    else :
        return False

if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
