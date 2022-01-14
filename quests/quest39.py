"""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number 
of characters then it should replace the missing second character of the final pair with an underscore ('_').
Examples:
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""


def solution(arr:str):
    if len(arr) %2 !=0:
        # x = arr[::-1]+"_"
        x = arr+"_"

        chunks = [x[i:i+2] for i in range(0, len(x), 2)]
        print(chunks)
        return chunks
    else:
        chunks = [arr[i:i+2] for i in range(0, len(arr), 2)]
        print(chunks)
        
        return chunks
        
arr  = "asdfads"

solution(arr)




