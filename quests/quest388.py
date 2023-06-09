
def not_order(data: list[int]) -> int:
    sorted_list = sorted(data)
    counter = 0
    for first , second in zip(sorted_list , data) :
        if first != second :
            counter +=1
    return (counter)
