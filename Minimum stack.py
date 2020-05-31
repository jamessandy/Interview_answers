#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 21:40:18 2020

@author: JammieSandy
"""

class MaxStack: 
    def __init__(self): 
          
       
        self.mainStack = []  
      
       
        self.trackStack = [] 
  
    def push(self, x): 
        self.mainStack.append(x)  
        if (len(self.mainStack) == 1): 
            self.trackStack.append(x)  
            return
  
       
        if (x > self.trackStack[-1]):  
            self.trackStack.append(x)  
        else: 
            self.trackStack.append(self.trackStack[-1]) 
  
    def Max(self): 
        return self.trackStack[-1] 
  
    def pop(self): 
        self.mainStack.pop()  
        self.trackStack.pop()
        
s = MaxStack() 
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.Max()) 
    
s.pop()
s.pop()
print(s.Max())