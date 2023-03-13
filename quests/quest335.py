"""
 Our Robo-Trio need to train for future journeys and treasure hunts. Stephan has built a special flat model of a pyramid. Now the robots can train for speed gold running. They start at the top of the pyramid and must collect gold in each room, choose to take the left or right path and continue down to the next level. To optimize their gold runs, Stephan need to know the maximum amount of gold that can be collected in one run.

Consider a list of lists in which the first list has one integer and each consecutive list has one more integer then the last. Such a list of lists would look like a pyramid. You should write a program that will help Stephan find the highest possible sum on the most profitable route down the pyramid. All routes down the pyramid involve stepping down and to the left or down and to the right.

Tips: Think of each step down to the left as moving to the same index location or to the right as one index location higher. Be very careful if you plan to use recursion here. 
"""
def count_gold(triangle):
    tr = [row[:] for row in triangle]  # copy
    for i in range(len(tr) - 2, -1, -1):
        for j in range(i + 1):
            tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])
    return tr[0][0]
