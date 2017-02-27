#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Code to generate gamma code as described as Integer Compression Methods
# Class 6 | 2/24/17 | 05-indexing.pdf [page 17]
#
# Integer Compression Methods
# • Binary: equal-length coding
#  – 3=>00000011; 5=>00000101
# • Unary: x³1 is coded as x-1 one bits followed
# by 0
#  – 3=> 110; 5=>11110
# • g-code: x=> unary code for 1 + |log x| followe
# by binary code for x-2 ^ |log x| in |log x| bits
#  – 3=>101, 5=>11001

import math

def binary(x,bit_len):
    binaryNum = bin(x).lstrip('0b').zfill(int(bit_len))
    print binaryNum

def unary(x):
    unary = "1"*(int(x)-1)+"0"
    print unary,

def gamma(x):
    unary(1 + math.log(x,2))
    binary(x - (2 ** int(math.log(x,2))), math.log(x,2))

# EXAMPLE
# – 2 10 0
# – 4 110 00
# – 14 1110 110
# – 63 111110 11111
# – 180 11111110 0110100
    
for x in [2,4,14,63,180]:
    print x
    gamma(x)
    print ''
