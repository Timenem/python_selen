"""
Unscramble the eggs.

The string given to your function has had an "egg" inserted directly after each consonant. You need to return the string before it became eggcoded.

Example
unscrambleEggs("Beggegeggineggneggeregg"); => "Beginner"

"""
def unscramble_eggs(word:str):
    return ("".join(word.split('egg')).strip())
