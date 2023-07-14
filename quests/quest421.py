def parse_IPv6(iPv6:str):
    spl_char = iPv6[4]
    spl_list = iPv6.split(spl_char)
    ans = []
    for i in spl_list:
        ans.append(str(sum([int(n,16) for n in i])))
    return ("".join(ans))

parse_IPv6("1234:5678:9ABC:D00F:1111:2222:3333:4445") #"10264228481217"
parse_IPv6("5454:FBFD:9ABC:AAAA:FFFF:2222:FBDE:0101") #"18544240608532"
parse_IPv6("0000:0000:0000:0000:0000:0000:0000:0000") #"00000000"
parse_IPv6("FFFF:FFFF:BBBB:CCCC:1212:AABC:0000:1111") #"6060444864304"
parse_IPv6("ACDD-0101-9ABC-AAAA-FFFF-2222-FBDE-ACCC") #"48242406085346"
parse_IPv6("5454rFBFDr9ABCrAA0ArFAFFr2222rFBDEr0101") #"18544230558532"
parse_IPv6("F234#5678#9ABC#D00F#1111#2222#3333#4485") #"24264228481221"
