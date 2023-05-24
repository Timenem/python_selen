def spacey(array: list[str]):
    ans = []
    word = ''
    for num, i in enumerate(array):
        word += array[num]
        ans.append(word)
    return ans
