import re

def balance_statement(lst):
    bad_formed, prices = [], {'B':0, 'S':0}
    for order in filter(None, lst.split(', ')):
        if not re.match('\S+ \d+ \d*\.\d+ (B|S)', order):
            bad_formed.append(order + ' ;')
        else:
            _, quantity, price, status = order.split()
            prices[status] += int(quantity) * float(price)
    ret = "Buy: %.0f Sell: %.0f" % (prices['B'], prices['S'])
    if bad_formed:
        ret += "; Badly formed %d: %s" % (len(bad_formed), ''.join(bad_formed))
    return ret
