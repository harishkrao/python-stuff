#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:40:12 2017

@author: Harish
"""

def listofdigits(inp):
    length_inp = len(str(inp))
    print(length_inp)
    output= []
    increment = int(str(1).zfill(len(str(inp)))[::-1])
    while increment >= 10:
        output.append(inp%increment/(increment/10))
        increment = increment / 10
    print(output)
        
    