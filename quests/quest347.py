"""
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.
Task

Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3
 b - 2
 s - 1

The right side letters and their power:

 m - 4
 q - 3
 d - 2
 z - 1

The other letters don't have power and are only victims.
Example

AlphabetWar("z");        //=> Right side wins!
AlphabetWar("zdqmwpbs"); //=> Let's fight again!
AlphabetWar("zzzzs");    //=> Right side wins!
AlphabetWar("wwwwwwz");  //=> Left side wins!
"""
def alphabet_war(fight: str) -> str:
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_score = 0
    right_score = 0
    for i in fight:
        if i in left.keys():
            left_score += left[i]
        elif i in right.keys():
            right_score += right[i]
    if left_score > right_score:
        return "Left side wins!"
    elif right_score > left_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"
