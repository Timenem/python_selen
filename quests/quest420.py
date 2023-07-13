def bits_war(n):
    e = sum([bin(i)[2:].count('1') if i>0 else -bin(i)[2:].count('1') for i in n if i%2==0])
    o = sum([bin(i)[2:].count('1') if i>0 else -bin(i)[2:].count('1') for i in n if i%2!=0])
    return "odds win" if o>e else "evens win" if e>o else 'tie'
