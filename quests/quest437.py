
def get_cell_addresses(cell_range:str)->[]:
    ans = []
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cell_range = cell_range.split(':')
    start = cell_range[0]
    end = cell_range[1]
    char_start = start[0]
    char_end = end[0]
    int_start = int(start[1:])
    int_end = int(end[1:])
    if char_start == char_end and int_start == int_end:
        return []
    elif ord(char_start) > ord(char_end):
        return []
    elif char_start == char_end:
        for i in range(int_start,int_end+1):
            ans.append(f"{char_start}{i}")
    else:
        index_start = CHARS.index(char_start)
        index_end = CHARS.index(char_end)
        CHARS = CHARS[index_start:index_end+1]
        for digit in range(int_start,int_end+1):
            for ch in CHARS:
                ans.append(f"{ch}{digit}")
    return ans
