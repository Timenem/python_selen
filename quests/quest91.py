"""
Nikola likes to categorize everything in sight. One time Stephan gave him a label maker for his birthday,
and the robots were peeling labels off of every surface in the ship for weeks. 
He has since categorized all the reagents in his laboratory, books in the library and notes on the desk. 
But then he learned about python dictionaries , and categorized all the possible configurations for Sophia’s drones.
Now the files are organized in a deep nested structure, but Sophia doesn’t like this. Let's help Sophia to flatten these dictionaries. 

"""

def translate(text: str) -> str:
    idx: int = 0
    result: list = []

    while idx < len(text):
        result.append(text[idx])

        if text[idx] in 'aeouiy':
            idx += 3
        elif text[idx].isspace():
            idx += 1
        else:
            idx += 2

    return ''.join(result)

  
if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
