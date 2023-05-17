
def reverse_vowels(s:str):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    vowels_position = [s.index(ch) for ch in s if ch in vowels ]
    a = ''
    counter = 0
    for ch in s :
        if ch not in vowels:
            a += ch
        elif ch in vowels:
            indx = vowels_position[::-1][counter]
            a += s[indx]
            counter +=1
    return (a)
