from sortingAlghoritm import BubbleSort
import unittest

rnd = [5, -2, 4, -1, 0]
answer = [-2, -1, 0, 4, 5]
reversAnswer = sorted(answer, reverse=True)


class TestSort(unittest.TestCase):
    def setUp(self):
        self.sortAlg = BubbleSort()

    def testForvardSort(self):
        self.assertEqual(self.sortAlg.forvardSort(rnd), answer)

    def testReversedSort(self):
        self.assertEqual(self.sortAlg.reveresdSort(rnd), reversAnswer)


if __name__ == '__main__':
    unittest.main()
