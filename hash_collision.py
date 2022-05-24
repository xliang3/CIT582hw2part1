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
    n = random.randint(1, 10000000)
    print(n)
    x = hashlib.sha256(n.encode('utf-8')).hexdigest()
    # n += 1
    # y = hashlib.sha256(n.encode('utf-8'))
    # while x[256-k:] != y[256-k:]:
    #     n += 1 
    #     y = hashlib.sha256(n.encode('utf-8'))
    # print(x, y)
    return( b'\x00',b'\x00' )



print(hash_collision)
