def points(games: list) -> int:
    point = 0
    for i in games:
        x = int(i[0])
        y = int(i[2])
        if x > y:
            point += 3
        elif x < y:
            point += 0
        else:
            point += 1
    return point
