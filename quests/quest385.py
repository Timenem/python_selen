from string import ascii_lowercase as lowers
def play_pass(s, n):
    shifted = lowers[int(n):] + lowers[:int(n)]
    t = s.maketrans(lowers, shifted)
    new_s = ""
    for i, char in enumerate(s):
        if char.isdigit():
            new_s += str(9-int(char))
        elif char.isalpha():
            new_s += [char.lower().translate(t).upper(), char.lower().translate(t).lower()][i % 2]
        else:
            new_s += char
    return new_s[::-1
