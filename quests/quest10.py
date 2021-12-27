"""
You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

"""

def between_markers(text: str, begin: str, end: str) -> str:
    if text.find(begin)==-1 and text.find(end)==-1:
        final= text
    elif text.find(begin)==-1:
        final= text[:text.find(end)]
    elif text.find(end)==-1:
        final= text[text.find(begin)+len(begin):]
    elif text.find(begin)>text.find(end):
        final= ''
    else:
        final= text[text.find(begin)+len(begin):text.find(end)]

    return final

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
