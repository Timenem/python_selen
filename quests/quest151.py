"""
This function creates an List of lists. that represents a two-dimensional grid with the given number of rows and cols.
This grid should contain the integers from start to start + rows * cols - 1 in ascending order, but the elements of every odd-numbered row have to be listed in descending order, so that when read in ascending order, the numbers zigzag through the two-dimensional grid.
Input: Two ints rows and cols. One optional argument start.
Output: List of lists. 
"""



def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    main_list = []
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(i*cols+j+start)
        if i%2:
            temp.sort(reverse = True)
        main_list.append(temp)
    return main_list
