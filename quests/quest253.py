def goes_after(word: str, first: str, second: str):
    try:
        first_indx = word.index(first)
        secnd_indx = word.index(second)
        if word == '':
            return False
        elif word[first_indx:secnd_indx + 1] == first + second:
            return True
        return False
    except ValueError:
        return False
