from typing import Iterable
def replace_biggest(data: list[int]) -> Iterable[int]:
    ans = []
    if len(data) ==0:
        return []
    else:
        counter = 1
        while counter < len(data): #or len(data) != 1:
            max_right_element = max(data[counter::])
            ans.append(max_right_element)
            counter +=1
        ans.append(-1)
        return (ans)
