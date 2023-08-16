def check_s_suffix(msg: str):
    if msg.endswith('s'):
        return msg[0:-1]
    else:
        return msg


def sursurungal(txt: str):
    quantity = int(txt.split(sep=' ')[0])
    msg = txt.split(sep=' ')[1]
    if quantity <= 1:
        return txt
    elif quantity == 2:
        msg = 'bu' + check_s_suffix(msg)
        # msg = 'bu'+msg
        return f"{quantity} {msg}"
    elif 3 <= quantity < 9:
        msg = check_s_suffix(msg) + 'zo'
        return f"{quantity} {msg}"
    elif quantity > 9:
        msg = 'ga' + check_s_suffix(msg) + 'ga'
        return f"{quantity} {msg}"
