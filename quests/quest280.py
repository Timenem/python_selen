"""
Dear Mr overseer,

we are delighted that they have still managed to us in time.

We have a big problem.

Mankind will be extinct in the near future. The cause!? - wars, diseases, natural disasters, aliens ... figure it out. But that’s not the point!

Vault-Tec has started to build vaults around the world. These are huge underground bunkers that allows us to survive. Your task is to select people and to populate with them these Vaults. We give you a population capacity and expect you to return the number of people that you want to put in these vaults.

However, there are several conditions that must be adhered to:

    A male overseer must always be present unless the capacity is 0
    If more than 50 dwellers move in, the overseer must have a wife (a "second overseer")
    With an even number of dwellers, the total number of men and women should be equal
    With an odd number of dwellers, the last free spot should be occupied by a woman

The mankind bets on you.

Good Luck

Your Vault-Tec Company

Vault-Tec Brochure
Examples

5 people   =>  1 Mr. Overseer, 3 female dwellers, 1 male dweller
51 people  =>  1 Mr. Overseer, 1 Mrs. Overseer, 25 female dwellers, 24 male dwellers

"""



def populate_my_vault(dwellers_count):
    if dwellers_count == 0:
        return 0, 0, 0
    elif dwellers_count == 1:
        return 1, 0, 0
    elif dwellers_count <= 50 and dwellers_count % 2 == 0:
        guard = 1
        womens = dwellers_count // 2
        mans = (dwellers_count // 2) - 1
        return guard, womens, mans
    elif dwellers_count <= 50 and dwellers_count % 2 != 0:
        guard = 1
        womens = (dwellers_count // 2) + 1
        mans = (dwellers_count // 2) - 1
        return guard, womens, mans
    elif dwellers_count > 50 and dwellers_count % 2 == 0:
        guards = 2
        womens = (dwellers_count // 2) - 1
        mans = (dwellers_count // 2) - 1
        return guards, womens, mans
    elif dwellers_count > 50 and dwellers_count % 2 != 0:
        guards = 2
        womens = (dwellers_count // 2)
        mans = (dwellers_count // 2) - 1
        return guards, womens, mans
