"""
 Your function must return this maximum possible profit for given price fluctuations. If it's not possible to make any profit with given prices (it's <= 0), your function should return 0.

Input: Stock prices as list of integers.

Output: Maximum possible profit as integer. 
"""



def stock_profit(stock: list[int]) -> int:

    prof = 0
    l = len(stock)
    for b_ind in range(l - 1):
        for s_ind in range(b_ind + 1, l):
            prof = max(prof, stock[s_ind] - stock[b_ind])

    return prof
