#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:39:36 2020

@author: JammieSandy
"""

def staircase(n):
    if n<= 1 :
        return n
    return staircase (n-1) + staircase(n-2)

def countways(s):
    return staircase(s + 1)

print (countways(4))
print (countways(5))