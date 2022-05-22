from itertools import product, combinations,permutations
from collections import namedtuple
def choose_best_sum(miles:int,cities:int,ls:list):
    random_cities = list(permutations(ls,cities))
    # maybe namedtuple
    rndCity = namedtuple(typename='city', field_names=['sumdistantion', 'ints'])
    # faster but failed
    a = [sum(i) for i in random_cities if sum(i) == miles]
    print(a[0])

    #failed time out
    # for distantion in list(random_cities):
        # cities = rndCity(sum(distantion),distantion )
        # if sum(distantion) == miles:
            # print(f"{sum(distantion)}:{distantion}")
            # return sum(distantion)


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
choose_best_sum(230, 4, xs) #230
# choose_best_sum(430, 5, xs) # 430)
# choose_best_sum(430, 8, xs) #None)
