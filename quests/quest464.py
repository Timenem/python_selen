
def alphabetized(s):
    new_order = sorted([char for char in s if char.isalpha()],key=str.lower)
    return ''.join(new_order)
