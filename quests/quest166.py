"""
Task:
Find out "B"(Bug) in a lot of "A"(Apple).

There will always be one bug in apple, not need to consider the situation that without bug or more than one bugs.

input: string Array apple

output: Location of "B", [x,y]
"""

def sc(lst:list):
    for i  in lst:
        if 'B' in i:
            return [lst.index(i),i.index('B')]
