"""
 You are given a word in which letters can be in different cases. Your task is to check whether the case was used correctly in the line. If everything is correct - return True, if there are errors - return False.

Examples of the correct use of cases:

All characters in the string are in uppercase. For example, "CHECKIO"
None of the characters are in uppercase. For example, "checkio"
Only the first character is in uppercase. For example, "Checkio"

Input: String.

Output: Bool.

Example:
assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True


"""

def correct_capital(s:str)->bool:
    if all([str(i).isupper() for i in s ]) or all([str(i).islower() for i in s[1::] ])  :
        return True
    else:
        return False
