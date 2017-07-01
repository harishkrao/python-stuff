#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:13:03 2017

@author: Harish
"""

def cumulative(inp):
    cum_list = []
    next = 0
    for each in inp:
        cum_list.append(each+next)
        next += each
    print(cum_list)