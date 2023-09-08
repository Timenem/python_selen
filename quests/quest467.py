def sort_the_pile(pile_of_towels:list[str], weekly_used_towels:list[int]):
    for quantity_of_towels in weekly_used_towels:
        dirty_towels = pile_of_towels[-quantity_of_towels::]
        pile_of_towels = pile_of_towels[:-quantity_of_towels]
        clean_towels = sorted(dirty_towels,reverse=True)
        pile_of_towels += clean_towels
    return pile_of_towels
