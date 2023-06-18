def prime_factor(n):
    i = 2
    int_list = []
    while i * i <= n:
        while n % i == 0:
            int_list.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        int_list.append(n)
    return int_list
