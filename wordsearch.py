#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:39:04 2020

@author: JammieSandy
"""

def word_search(matrix, word):
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if WordFind(matrix, col, row, word):
				print("Found", word, "with first letter in row", row+1, "and column", col+1)
				return True
	print("Word not found.")
	return False

def WordFind(matrix, col, row, word):
	
	if matrix[row][col] != word[0]:
		return False 
	
	for i in range(len(x)):
		
		rd = row + x[i]
		
		cd = col + y[i]
		
		for k in range(1, len(word)):
			
			if (rd >= len(matrix) or rd < 0 or cd >= len(matrix[0]) or cd < 0):
				break
			#if the word no longer matches the characters in the grid, quit looking
			if matrix[rd][cd] != word[k]:
				break
			
			rd += x[i]
			cd += y[i]
			
			if k == len(word)-1:
				return True 
	
	return False 

x = [-1, 0, 1, 0]
y = [0, -1, 0, 1]

matrix = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S'],
 ['T', 'E', 'S', 'T']]

print(word_search(matrix, "FOAM"))


