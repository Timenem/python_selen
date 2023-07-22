def ip_to_num(ip:str):
    ints = "".join(["{0:b}".format(int(i)).zfill(8) for i in ip.split('.')])
    return int(ints, 2)


import socket, struct
def num_to_ip(ip):
    return socket.inet_ntoa(struct.pack('!L',ip))
