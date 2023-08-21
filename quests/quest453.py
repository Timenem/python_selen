
def get_participants(handshakes: int):
    farmers = 0
    while handshakes > farmers * (farmers - 1) / 2:
        farmers += 1
    return farmers
