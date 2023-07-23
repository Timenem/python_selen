
def yes_no(arr:list):
    for r in range(1, len(arr) - 1):
        arr.append(arr.pop(r))
    return arr
