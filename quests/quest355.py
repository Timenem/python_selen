"""
Write a function insert_dash(num) / insertDash(num) / InsertDash(int num) that will insert dashes ('-') between each two odd digits in num. For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd digit.

Note that the number will always be non-negative (>= 0).

"""
def insert_dash(num):

    digits = [d for d in str(num)]
    for i in range(len(digits)-1):
        if int(digits[i])%2 and int(digits[i+1])%2:
            digits[i] = digits[i] + '-'

    return ''.join(digits)
