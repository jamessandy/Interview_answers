#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:43:56 2020

@author: JammieSandy
"""

class Solution:
  def calculate(self, s: str) -> int:
    self.pos = 0    
    def eval():
      val = 0
      sign = 1
      ret = 0
      while self.pos < len(s):
        ch = s[self.pos]
        if ch == ' ':
          self.pos += 1
        elif ch == '(':
          self.pos += 1
          val = eval()
        elif ch == ')':
          self.pos += 1
          ret += sign * val
          return ret
        elif ch == '+' or ch == '-':
          ret += sign * val
          val = 0
          sign = 1 if ch == '+' else -1
          self.pos += 1
        else:
          val = val * 10 + (ord(ch) - ord('0'))
          self.pos += 1
      ret += val * sign
      return ret
    return eval()

print (eval('-(3+(2-1))'))