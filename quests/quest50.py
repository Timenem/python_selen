'''
Вводятся данные в формате ключ=значение в одну строчку через пробел. Значениями здесь являются целые числа (см. пример ниже).
Необходимо на их основе создать словарь d с помощью функции dict() и вывести его на экран командой:

'''

x = input().split()
nums = []
strs = []
for i in x:
    nums.append(int(i[-1]))
    strs.append(str(i[0:i.index("=")]))

d = dict(zip(strs,nums))
print(*sorted(d.items()))

