def check_tombola(sheet):
    if not (len(sheet) == 3 and all(len(r) == 9 for r in sheet)):
        return False
    if len(set(sum((list(filter(lambda x: x != 0, r)) for r in sheet), []))) != 15:
        return False
    if not all(len(list(filter(lambda x: x != 0, r))) == 5 for r in sheet):
        return False
    ranges = [range(1, 10), range(10,20), range(20, 30), range(30, 40), range(40, 50), range(50, 60), range(60, 70), range(70, 80), range(80, 91)]
    for i in range(9):
        if not list(filter(lambda x: x != 0, [sheet[j][i] for j in range(3)])):
            return False
        if sorted(list(filter(lambda x: x != 0, [sheet[j][i] for j in range(3)]))) != list(filter(lambda x: x != 0, [sheet[j][i] for j in range(3)])):
            return False
        if not all(r in ranges[i] for r in filter(lambda x: x != 0, [sheet[j][i] for j in range(3)])):
            return False
    return True
