
import re
def autocorrect(s:str):
    s = s.lower()
    return re.sub(pattern=r"\b(you+|u)\b", repl="your sister", string=s,flags=re.IGNORECASE)

