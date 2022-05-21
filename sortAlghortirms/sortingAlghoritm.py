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

    
    
 class InsertionSort:
    def insertSort(self, randomIntegerList:List[int]):
        n = len(randomIntegerList)
        for i in range(1 ,n):
            currentVal = randomIntegerList[i]
            j = i -1
            while j >=0:
                if currentVal < randomIntegerList[j]:
                    randomIntegerList[j+1] = randomIntegerList[j]
                    randomIntegerList[j] = currentVal
                    j = j-1
                else:
                    break
        return randomIntegerList

   
