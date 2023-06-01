
def wave(people:str)->list[str]:
    answer = []
    for index, w in enumerate(people):
        if w.isalpha():
            answer.append(people[:index]+people[index].upper()+people[index+1:])
    return answer
