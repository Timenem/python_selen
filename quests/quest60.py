"""
На вход поступает строка из целых чисел, записанных через пробел.
С помощью функции map преобразовать эту строку в список целых чисел, взятых по модулю.
Сформируйте именно список lst из таких чисел.
Отобразите его на экране в виде набора чисел, идущих через пробел.
"""

x =input().split(" ")
int_nums = list(map(int,x))
absval = list(map(abs,int_nums))
print(*absval)

# print(*[abs(n) for n in list(map(int, input().split()))])