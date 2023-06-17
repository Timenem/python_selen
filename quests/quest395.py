import re 

def decode(s:str)->str:
    splited  = re.match(r"([0-9]+)([a-zA-Z]+)",s).groups()
    integer = int(splited[0])
    chars = splited[1]
    word = ''
    for ch in chars:
        for i in range(26):
            if i * integer % 26 == (ord(ch) - 97):
                word += chr(i + 97)
    if len(word) == len(chars):
        return word
    else:
        return "Impossible to decode"
