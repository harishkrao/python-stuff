#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 21:27:18 2017

@author: Harish
"""
def sum67(nums):
  sum_nums = 0
  sum_67 = 0
  for i in range(len(nums)):
    sum_nums += nums[i]
    print(i)
  k = 0
  for m in range(len(nums)):
      if nums[m] == 7:
          k = m
  print('7',k)
  for j in range(nums.index(6),k):
    sum_67 += nums[j]
  print(sum_nums)
  print(sum_67)
  


  
        
    
   
                
            