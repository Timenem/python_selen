
import re


def calculator(log: str) -> str:
    p = re.compile("\d+|[+-=]")
    digits = re.findall(p, log)
    curr_n =0
    n = 0
    op = "+"
    for symbol in digits:
        if symbol.isdigit():
            curr_n = int(symbol)
        elif symbol in ["+", "-", "="]:
            if op == "+":
                curr_n = n + curr_n
                op = symbol
            elif op == "-":
                curr_n = n - curr_n
                op = symbol
            n = curr_n
    return str(curr_n)
