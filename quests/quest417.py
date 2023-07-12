import sys


def fizz_buzz_custom(string_one: str = "Fizz", string_two: str = "Buzz", num_one: int = 3, num_two: int = 5):
    return [string_one * (not i % num_one) + string_two * (not i % num_two) or i for i in range(1, 101)]
