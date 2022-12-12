def prev_mult_of_three(n:int):
    x = int(n)
    while len(str(x)) !=0:
        try:
            if x %3 ==0:
                print (x)
                return x
            else:
                x = int(str(x)[:-1])
        except ValueError:
            return None
