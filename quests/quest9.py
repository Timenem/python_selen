""" You have a number and you need to determine which digit in this number is the biggest. """

def max_digit(number: int) -> int:
    s = str(number)
    l = []
    n = [l.append(int(i))  for i in s]
    m = max(l)
    return m

if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
