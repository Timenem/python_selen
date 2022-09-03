def eval_expression(arr:str):
    stack=[]
    operators=["+","-","*","/"]

    for item in arr.split(' '):
        if item not in operators:
            stack.append((item))
        else:
            first=int(stack.pop())
            sec=int(stack.pop())

            if(item=="+"):
                stack.append(sec + first)

            if (item == "-"):
                stack.append(sec - first)

            if (item == "*"):
                stack.append(sec * first)

            if (item == "/"):
                stack.append(sec / first)
    return stack[-1]
