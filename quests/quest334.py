"""
Every Turkish citizen has an identity number whose validity can be checked by these set of rules:

    It is an 11 digit number
    First digit can't be zero
    Take the sum of 1st, 3rd, 5th, 7th and 9th digit and multiply it by 7. Then subtract the sum of 2nd, 4th, 6th and 8th digits from this value. Modulus 10 of the result should be equal to 10th digit.
    Sum of first ten digits' modulus 10 should be equal to eleventh digit.

"""

def check_valid_tr_number(number):
    if len(str(number)) != 11 or type(number) == str:
        return False
    elif str(number).startswith('0'):
        return False
    else:
        lst_digits = [int(i) for i in str(number)]
        odd = sum([int(lst_digits[0]), int(lst_digits[2]), int(lst_digits[4]), int(lst_digits[6]), int(lst_digits[8])]) * 7
        even = sum([int(lst_digits[1]), int(lst_digits[3]), int(lst_digits[5]), int(lst_digits[7])])
        tens = sum(lst_digits[:10])
        if abs(odd - even) % 10 == lst_digits[9] and tens % 10 == lst_digits[-1]:
            return True
        else:
            return False
