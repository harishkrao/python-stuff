#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:44:34 2017

@author: Harish
"""
#
wordlist = ['cat','dog','rabbit']
sample_list = [1,2,3,4,5,6,7,8,9]
#letterlist = []
#for aword in wordlist:
#    while aletter in aword:
#        letterlist.append(aletter)
#print(letterlist)

list_inp = []

def oddpos(list_inp):
    i = 0
    while i in range(len(list_inp)):
        print(list_inp[i])
        i+=2
            
oddpos(sample_list)

def evenpos(list_inp):
    i = 1
    while i in range(len(list_inp)):
        print(list_inp[i])
        i+=2
        
evenpos(sample_list)
        