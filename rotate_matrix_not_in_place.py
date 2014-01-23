"""
rotate_matrix_not_in_place.py clockwise
"""

def rotate(matrix):
    n = len(matrix)
    new_matrix = []
    for i in range(n):
        new_matrix.append(list(matrix[i]))
    for r in range(n):
        for c in range(n):
            new_matrix[c][(-1)-r] = matrix[r][c]
    for row in new_matrix:
        print row

matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotate(matrix1)