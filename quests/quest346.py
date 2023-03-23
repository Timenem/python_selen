"""
Convert a number to a binary coded decimal (BCD).

You can assume input will always be an integer. If it is a negative number then simply place a minus sign in front of the output string. Output will be a string with each digit of the input represented as 4 bits (0 padded) with a space between each set of 4 bits.

Ex.

n =  10 -> "0001 0000"
n = -10 -> "-0001 0000"


"""
def to_bcd(n: int) -> str:
    if n < 0:
        return '-' + " ".join([format(int(i), "0>4b") for i in str(abs(n))])
    else:
        return " ".join([format(int(i), "0>4b") for i in str(n)])
