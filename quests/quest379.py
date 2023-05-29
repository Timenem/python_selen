import math 
def sum_square_even_root_odd(nums):
    ans = 0
    for num in nums :
        if num %2==0:
            ans += num**2
        else:
            ans += math.sqrt(num)
    return (round(ans,2))
