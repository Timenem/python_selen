"""
 You are given a dictionary, where keys and values are strings. Your function should return a dictionary as well, where keys and values from input dictionary are switched: input keys become output values and vice versa. Looks easy? It is so! The only thing left to mention: the values in the result dictionary should be sets (so the input key(s) - the element(s) of the set). Good luck!

Input: A dictionary.

Output: A dictionary.

Examples:
assert switch_dict({"rouses": "red", "car": "red", "sky": "blue"}) == {
    "red": {"car", "rouses"},
    "blue": {"sky"},
}
assert switch_dict({"1": "one", "2": "two", "3": "one", "4": "two"}) == {
    "one": {"3", "1"},
    "two": {"4", "2"},
}
assert switch_dict({"a": "b", "b": "c", "c": "a"}) == {
    "b": {"a"},
    "c": {"b"},
    "a": {"c"},
}

"""

def switch_dict(data : dict[str, str]) -> dict:
    data_names = set(data.values())
    d = {}
    for n in data_names:
        d[n] = tuple([k for k in data.keys() if data[k] == n])
    return d
