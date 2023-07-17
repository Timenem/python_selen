
import re

def money_value(s:str):
    r = re.findall(pattern='[^$ +]',string=s.strip())
    try:
        return float("".join(r))
    except:
        return 0.0
