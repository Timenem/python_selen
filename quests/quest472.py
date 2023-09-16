def create_iterator(func, n):
    def f(a):
        r=a
        for i in range(0,n):
            r=func(r)
        return r
    return f
