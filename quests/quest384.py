def is_ore(n):
    sum=0
    count=0
    for divisor in range(1, int(n/2)+1):
        if n%divisor == 0:
            count += 1
            sum += divisor
    if n*count%sum == 0:
        return True
    return False
