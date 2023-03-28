"""
A keyword cipher is a monoalphabetic cipher which uses a "keyword" to provide encryption. It is somewhat similar to a Caesar cipher.

In a keyword cipher, repeats of letters in the keyword are removed and the alphabet is reordered such that the letters in the keyword appear first, followed by the rest of the letters in the alphabet in their otherwise usual order.

E.g. for an uppercase latin alphabet with keyword of "KEYWORD":

A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z

becomes:

K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z

such that:

cipher.encode('ABCHIJ') == 'KEYABC'
cipher.decode('KEYABC') == 'ABCHIJ'

All letters in the keyword will also be in the alphabet. For the purpose of this kata, only the first occurence of a letter in a keyword should be used. Any characters not provided in the alphabet should be left in situ when encoding or decoding.

"""
from string import maketrans

class keyword_cipher(object):
    def __init__(self, abc, keyword):
        key_abc = ''.join(sorted(set(keyword), key=keyword.index)) + ''.join(c for c in abc if c not in keyword)
        self.e_tab = maketrans(abc, key_abc)
        self.d_tab = maketrans(key_abc, abc)
    def encode(self, str):
        return str.translate(self.e_tab)
    def decode(self, str):
        return str.translate(self.d_tab)
    
    
    from string import ascii_lowercase
class keyword_cipher(object):
    def __init__(self, abc, keyword):
        self.abc = abc
        self.keyword = keyword

    def remove_duplicate(self) -> str:
        finish_str = []
        for i in self.keyword:
            if i not in finish_str:
                finish_str.append(i)
        for ch in ascii_lowercase:
            if ch not in finish_str:
                finish_str.append(ch)
        return "".join(finish_str)


    def encode(self,plain: str) -> str:
        rem_dupl = self.remove_duplicate()
        d = dict(zip(ascii_lowercase, rem_dupl))
        ans = ''
        for ch in plain:
            ans += d[ch]
        return ans

    def decode(self,ciphered:str):
        rem_dupl = self.remove_duplicate()
        d = dict(zip(rem_dupl,ascii_lowercase))
        ans = ''
        for ch in ciphered:
            ans += d[ch]
        return ans

