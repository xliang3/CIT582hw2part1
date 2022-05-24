import hashlib
import os
import random

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here

    def helper(code):
        dic = {'0': '0000', 
               '1': '0001', 
               '2': '0010', 
               '3': '0011',
               '4': '0100',
               '5': '0101',
               '6': '0110',
               '7': '0111',
               '8': '1000',
               '9': '1001',
               'a': '1010',
               'b': '1011',
               'c': '1100',
               'd': '1101',
               'e': '1110',
               'f': '1111'}
        s = ''
        for letter in code:
            s += dic[letter]
        print(s)
        return s[256-k:]


    n = random.randint(1, 10000000)
    x = str(n).encode('utf-8')
    x_code = hashlib.sha256(x).hexdigest()
    print(type(x_code), x_code)
    x_str = helper(x_code)
    # n += 1
    # y = str(n).encode('utf-8')
    # y_code = hashlib.sha256(y).hexdigest()
    # y_str = helper(y_code)
    # while x_str != y_str:
    #     n += 1
    #     y = str(n).encode('utf-8')
    #     y_code = hashlib.sha256(y).hexdigest()
    #     y_str = helper(y_code)
    return( b'\x00',b'\x00' )


