
import re
def camelize(string:str)->str:
    return "".join(i.capitalize() for i in re.findall(r"[A-Za-z0-9]*",string))
