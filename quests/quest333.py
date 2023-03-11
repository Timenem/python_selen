
def computer_to_phone(numbers:str):
    ans = []
    for i in numbers:
        if i == '0':
            ans.append('0')
        elif i == '1':
            ans.append('7')
        elif i == '2':
            ans.append('8')
        elif i == '3':
            ans.append('9')
        elif i == '4':
            ans.append('4')
        elif i == '5':
            ans.append('5')
        elif i == '6':
            ans.append('6')
        elif i == '7':
            ans.append('1')
        elif i == '8':
            ans.append('2')
        elif i == '9':
            ans.append('3')
    return "".join(ans)

def computer_to_phone(numbers):
    return numbers.translate(str.maketrans('123789', '789123'))
