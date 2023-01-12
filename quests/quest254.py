"""


Nicola likes to categorize all sorts of things. He categorized a series of numbers and as the result of his efforts, a simple sequence of numbers became a deeply-nested list. Sophia and Stephan don't really understand his organization and need to figure out what it all means. They need your help to understand Nikolas crazy list.

There is a list which contains integers or other nested lists which may contain yet more lists and integers which then… you get the idea. You should put all of the integer values into one flat list. The order should be as it was in the original list with string representation from left to right.
In this mission you should use the 'yield' to make your function a generator. 
"""


def flat_list(array):
    items = list(array)
    while items:
        item = items.pop(0)
        if hasattr(item, '__iter__'):
            i = [x for x in item]
            items = i + items
        else:
            yield item
