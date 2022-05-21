from typing import List


class BubbleSort:
    def forvardSort(self, randomIntegerList: List[int]):
        n = len(randomIntegerList)
        for i in range(n):
            for j in range(n - i - 1):
                if randomIntegerList[j] > randomIntegerList[j + 1]:
                    randomIntegerList[j], randomIntegerList[j + 1] = randomIntegerList[j + 1], randomIntegerList[j]
        return randomIntegerList

    def reveresdSort(self, randomIntegerList: List[int]):
        n = len(randomIntegerList)
        for i in range(n):
            for j in range(n - i - 1):
                if randomIntegerList[j] < randomIntegerList[j + 1]:
                    randomIntegerList[j], randomIntegerList[j + 1] = randomIntegerList[j + 1], randomIntegerList[j]
        print(randomIntegerList)
        return randomIntegerList
