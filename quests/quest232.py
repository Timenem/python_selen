"""
DESCRIPTION:
Introduction
Both the IPv4 address and subnet mask is made up of 32 bits. The bits are divided into four sections called octets (groups of eight). Each octet can have a number in the range 0 to 255 (unsigned 8-bit integers).

When learning IPv4 addressing it is essential to know how the Binary Number System works as well as having the right tools for the task you are facing. But, you are lacking a good peace of code to visualize the IPv4 addresses and subnet masks in binary form...

The Assignment
Your task is to implement a funtion def ipv4_to_binary(ipv4_addr: str) -> str which takes in an IPv4 address ipv4_addr, converts it into Dotted Binary Notation and returns it as a string.

Here are a few examples of input (left) and output (right):

192.168.0.33    = 11000000.10101000.00000000.00100001
255.255.255.0   = 11111111.11111111.11111111.00000000

10.55.0.13      = 00001010.00110111.00000000.00001101
255.255.255.252 = 11111111.11111111.11111111.11111100
"""
def ipv4_to_binary(ipv4_addr: str) -> str:
    a = ''
    for i in ipv4_addr.split('.'):
        a += ' ' + format(int(i), '08b')
    return a.strip().replace(' ', '.')
