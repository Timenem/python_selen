"""
Create a function that converts a given ASCII string to its hexadecimal SHA-256 hash.
"""

import hashlib
def to_sha256(s:str)->str:
    a = hashlib.sha256(s.encode('utf-8')).hexdigest()
    return (a)

