"""

Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord


"""


def camel_case(s:str):
    m = []
    for i in s.split(sep=' '):
        m.append( i.title())
    return ("".join(m))
