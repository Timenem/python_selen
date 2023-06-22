from collections import Counter
import re
def validate_bet(game: list[int], text: str):
    not_allowed = [";",":","'","."]
    for i in  text:
        if i in not_allowed:
            return None
    else:
        digits = [int(i) for i in re.findall(r"\d+",text)]
        c = dict(Counter(digits))
        max_val = game[1]
        len_arr = game[0]
        if any(i >=2 for i in c.values()):
            return None
        elif len(digits) < len_arr:
            return None
        elif any(digit > max_val or digit<1 for digit in digits):
            return None
        elif len(set(digits)) != len_arr:
            return None
        else:
            return digits
