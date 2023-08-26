
def turn90(cipher_grille):
    grille=[]
    cipher_grille = zip(cipher_grille[0],cipher_grille[1],cipher_grille[2],cipher_grille[3])
    for x in cipher_grille:
        a=''.join(x)
        grille.append(a[::-1])
    return grille

def decode(code, cipheredPassword, decipheredPassword ):
    stringCode = ""
    for line in code:
        stringCode+=line
    for i in range(0, 16):
        if stringCode[i] == 'X':
            decipheredPassword += cipheredPassword[i]
    return decipheredPassword

def recall_password(cipher_grille, ciphered_password):
    cipheredPassword = ""
    for line in ciphered_password:
        cipheredPassword += line
    decipheredPassword=""
    for i in range(0,4):
        decipheredPassword = decode(cipher_grille, cipheredPassword, decipheredPassword)
        cipher_grille = turn90(cipher_grille)
    return decipheredPassword
