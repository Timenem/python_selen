def get_turkish_number(num: int):
    zero_nine = {
        0: 'sifir',
        1: 'bir',
        2: 'iki',
        3: 'üç',
        4: 'dört',
        5: 'beş',
        6: 'alti',
        7: 'yedi',
        8: 'sekiz',
        9: 'dokuz',
    }
    ten_nineteen = {
        10:"on",
        20:"yirmi",
        30:"otuz",
        40:"kirk",
        50:"elli",
        60:"altmiş",
        70:"yetmiş",
        80:"seksen",
        90:"doksan",
    }
    str_num = str(num)
    if len(str_num) <2:
        return zero_nine.get(num)
    else:
        first = int(str(num)[0])*10
        second = int(str(num)[1])
        return f"{ten_nineteen.get(first)} {zero_nine.get(second)}"
