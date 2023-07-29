def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1.name:
        first = fighter1
        second = fighter2
    else:
        first = fighter2
        second = fighter1
    while first.health > 0:
        second.health -= first.damage_per_attack
        first, second = second, first
    return second.name

