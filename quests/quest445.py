def min_distance(n):
    factors = [i for i in range(1, n + 1) if n % i == 0]
    rs = min([factors[i+1]-factors[i] for i in range(len(factors)-1)])
    return rs
  
