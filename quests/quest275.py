"""
Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.
Example (input -> output):

'this is a string!!' -> 'dGhpcyBpcyBhIHN0cmluZyEh'

You can learn more about Base64 encoding and decoding here.

Note: This kata uses the non-padding version ("=" is not added to the end).

"""

import base64

def to_base_64(string):
    return base64.b64encode(string.encode('ascii')).decode('ascii').replace('=', '')

def from_base_64(string):
    string += '=' * (len(string) % 4)
    return base64.b64decode(string.encode('ascii')).decode('ascii')
