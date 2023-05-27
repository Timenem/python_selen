def find_hack(arr):
    ans = []
    points = {"A": 30, "B": 20, "C": 10, "D": 5}
    for i in arr:
        total_balls = 0
        bonus = 20
        for x in i[2]:
            total_balls += points.get(x, 0)
            if (points.get(x, 0) != 30 and points.get(x, 0) != 20) or len(i[2]) < 5:
                bonus = 0
        total_balls += bonus
        if total_balls > 200:
            total_balls = 200
        if total_balls != i[1]:
            ans.append(i[0])
    return ans
