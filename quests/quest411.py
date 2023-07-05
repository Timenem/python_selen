import hashlib
# simple hashlib
def checkio(hashed_string, algorithm):
    return getattr(hashlib, algorithm)(hashed_string.encode()).hexdigest()
