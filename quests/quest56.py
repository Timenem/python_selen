
def time_converter(time):
        
    if time[:2] == "00":
        hour = "12"
    elif int(time[:2]) < 13:
        hour = str(int(time[:2]))       
    else:
        hour = str(int(time[:2])-12)

    part = ' a.m.' if int(time[:2]) < 12 else ' p.m.'    
    time = hour + ":" + time[3:] + part

    return time


if __name__ == '__main__':
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
