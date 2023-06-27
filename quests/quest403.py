def changing_direction(elements: list[int]) -> int:

    dir = count = 0
    for a, b in zip(elements, elements[1:]):
        dir2 = a - b
        if dir2:
            if dir2 * dir < 0:
                count += 1
            dir = dir2

    return count

print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
