
import re
def is_valid_HK_phone_number(number):
    a = re.fullmatch(pattern=r"[0-9]{4}\s[0-9]{4}", string=number)
    return True if a else False


def has_valid_HK_phone_number(number):
    a = re.findall(pattern=r"[0-9]{4}\s[0-9]{4}", string=number)
    return True if len(a) >0 else False
