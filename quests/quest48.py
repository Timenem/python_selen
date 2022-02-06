"""
Stephan and Sophia forget about security and use simple passwords for everything.
Help Nikola develop a password security check module. The
password will be considered strong enough if its length is greater than or equal to 10 symbols,
it has at least one digit,
as well as containing one uppercase letter and one lowercase letter in it.
The password contains only ASCII latin letters or digits.
"""
def checkio(data):
    digit, upper, lower = False, False, False
    if len(data) < 10:
        return False
    else:
        for i in data:
            if i.isdigit():
                digit = True
            elif i.islower():
                lower = True
            elif i.isupper():
                upper = True
        if digit and lower and upper:
            return True
        else:
            return False

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
