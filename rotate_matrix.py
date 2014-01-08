""" 
Given an NxN matrix, rotate the matrix by pi/2
"""

matrix_1 = [["a", "b", "c", "d"],
["e", "f", "g", "h"],
["i", "j", "k", "l"],
["m", "n", "o", "p"]]

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n//2):
        temp = matrix[i]








print rotate_matrix(matrix_1)