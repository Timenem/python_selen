"""

Write a function deNico/de_nico() that accepts two parameters:

    key/$key - string consists of unique letters and digits
    message/$message - string with encoded message

and decodes the message using the key.

First create a numeric key basing on the provided key by assigning each letter position in which it is located after setting the letters from key in an alphabetical order.

For example, for the key crazy we will get 23154 because of acryz (sorted letters from the key).
Let's decode cseerntiofarmit on  using our crazy key.

1 2 3 4 5
---------
c s e e r
n t i o f
a r m i t
  o n   

After using the key:

2 3 1 5 4
---------
s e c r e
t i n f o
r m a t i
o n

Notes

    The message is never shorter than the key.
    Don't forget to remove trailing whitespace after decoding the message


deNico("crazy", "cseerntiofarmit on  ") => "secretinformation"
deNico("abc", "abcd") => "abcd"
deNico("ba", "2143658709") => "1234567890"
deNico("key", "eky") => "key" 
"""

def de_nico(key, message):
    key_length = len(key)
    order = [sorted(key).index(character) for character in key]
    split_message = [message[i:i+key_length] for i in range(0, len(message), key_length)]

    decoded_message = ""

    for part in split_message:
        for index in order:
            if index < len(part):
                decoded_message += part[index]

    return decoded_message.rstrip()
