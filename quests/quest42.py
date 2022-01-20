"""
Анаграммы - это игра со словами, 
в которой переставляя в словах или фразах буквы местами, 
мы получаем новые слова или фразы. 
Два слова анаграммы друг для друга,
если одно можно получить из другого перестановкой букв. 
Также для анаграмм регистр букв и пробелы не имеют значения. 
Для примера, "Gram Ring Mop" и "Programming" -- анаграммы.
Но вот "Hello" и "Ole Oh" уже нет.
Итак, вам даны два слова или фразы.
Попробуйте определить анаграммы ли они друг для друга. 
"""

def verify_anagrams(a, b):
    sort_a = "".join(sorted(a.lower()))
    sort_b = "".join(sorted(b.lower()))
    if sort_a.lstrip() == "".join(sort_b).lstrip():
        return True
    else:
        return False



if __name__ == '__main__':
    print("Example:")
    assert verify_anagrams('Programming', 'Gram Ring Mop') == True
    assert verify_anagrams('Hello', 'Ole Oh') == False
    assert verify_anagrams('A O X','x o a') == True
    assert verify_anagrams('Kyoto', 'Tokyo') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")