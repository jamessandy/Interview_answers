#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:40:18 2020

@author: JammieSandy
"""
def witnesses(heights):
    max_height = float('-inf')
    total = 0
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > max_height:
            total += 1
        max_height = max(heights[i], max_height)
    return total


print(witnesses([3, 6, 3, 4, 1]))
