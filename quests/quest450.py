
def balance(left: str, right: str):
    left = sum([int(i) for i in left.replace('!', '2').replace('?', '3')])
    right = sum([int(i) for i in right.replace('?', '3').replace('!', '2')])
    if left == right:
        return 'Balance'
    elif left > right:
        return 'Left'
    else:
        return 'Right'
