#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:16:22 2017

@author: Harish
"""

#==============================================================================
def per(inp):
    sorted_input = sorted(inp)
    for i in range(len(inp)):
        print(inp[i],'percentile = ',100*((sorted_input.index(inp[i])+1)-0.5)/len(inp))
#==============================================================================

#==============================================================================
def bubble(a):
    changed = True
    while changed:
        changed = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                print(a)
                changed = True
    print(a)
 
#==============================================================================
    
#==============================================================================
def manual_sort(a):
    sorted_output = []
    while a:
        minimum_element = a[0]
        for  i in range(len(a)):
            if a[i] < minimum_element:
                minimum_element = a[i]
            #print(a[i],minimum_element,a,sorted_output)
        sorted_output.append(minimum_element)
        a.remove(minimum_element)
    
        
    return sorted_output
    
#==============================================================================
a1 = [2,1,0,9,7,4,3,1,7]
    
#==============================================================================
def msearch(a,search):
    found = 0
    if len(a) == 0:
        return False
    elif len(a) >= 1:
        for i in range(len(a)):
            if a[i] == search:
                found = 1
    if found == 1:
        return True
    else:
        return False
#     
#==============================================================================

#==============================================================================
def bsearch(a,search):
    #found = 0
    if len(a) == 0:
        return False
    else:
        mid = len(a)//2
        if search == a[mid]:
            return True
        else:
            if search > a[mid]:
                return bsearch(a[mid+1:],search)
            elif search < a[mid]:
                return bsearch(a[:mid],search)
#==============================================================================
    
#==============================================================================
def histo(st):
    dict1 = {}
    list1 = st.split()
    for word in list1:
        dict1[word] = dict1.get(word,0) + 1
    #print(dict1)
    list1.clear()
    for (k,v) in dict1.items():
        list1.append((k,v))
    #print(list1)
    list2 = []
    for (k,v) in list1:
        list2.append((v,k))
    list2.sort(reverse = True)
    print(list2)

    for (k,v) in list2:
        #print(str(v).rjust(len(str(v))-10),k*'#')
        print(v.rjust(20),k*'#')
#==============================================================================

#==============================================================================
from collections import Iterable

def flat(inp, output = []):
        
    for i in inp:
        if isinstance(i,Iterable):
            flat(i,output)
        else:
            output.append(i)
    return output
#==============================================================================
