units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tenth = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens  = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
powers = ["thousand"] + [pre + "illion" for pre in ["m", "b", "tr", "quadr", "quint", "sext", "sept", "oct", "non", "dec"]]

def wordify(n):
    '''String representation of a number n under 10^36'''
    if n < 0: return "minus " + tell_number(-n)
    if n == 0: return "zero"
    for p in range(len(powers), 0, -1):
        d, m = divmod(n, 1000 ** p)
        if d: return tell_number(d) + " " + powers[p-1] + (" " + tell_number(m)) * (m>0)
    h, t, u = map(int, "%03d" % n)
    triplet = [units[h], "hundred" * (h>0), tens[t], [units, tenth][t == 1][u]]
    return " ".join(filter(None, triplet))
