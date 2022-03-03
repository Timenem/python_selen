import datetime

def friday(day):
    d = datetime.datetime.strptime(day, "%d.%m.%Y")
    week_day = d.weekday()
    answer = 4 - week_day
    return abs(answer)

if __name__ == '__main__':
    print("Example:")
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
