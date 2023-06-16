import  re

def get_symbol(line:str):
    a = re.findall("[-]\d",line)
    if len(a) ==0:
        return ''
    else:
        return '-'

def number_type(s:str)->int|float:
    if '.' in s :
        return float(s)
    else:
        return int(s)

def reveal_num(line: str) -> int | float | None:
    ans = []
    allowed_chars = ['.', '-', '+']
    symbol = get_symbol(line)
    for index, i in enumerate(line):
        if i.isdigit() or i in allowed_chars and i not in ans:
            ans.append(i)
    ans = "".join(ans).replace('-', '').replace('+', '')
    if len(ans) == 0:
        return None
    else:
        number = number_type(ans)
        if symbol =='-':
            ans = -abs(number)
            return ans
        else:
            return int(ans)
