
def encrypt_this(test:str)->str:
    splitted_text = test.split(sep=' ')
    first_index = 0
    second_index = 1
    last_index = -1
    answer = []
    for word in splitted_text :
        if len(word) == 1:
            answer.append(str(ord(word)))
        elif len(word) == 2:
            answer.append(str(ord(word[first_index]))+word[last_index])
        elif len(word) > 2:
            first = str(ord(word[0]))
            second = word[last_index]
            last = word[second_index]
            word = first+second+word[2:-1]+last
            answer.append(word)
    return " ".join(answer)
