"""
Given a matrix, print diagonal lines
Ex: [[1  2  3  4],
     [5  6  7  8],
     [9  1  2  3]]
print:
1
52
963
17
28
3
"""

def authorize(row, column, total_rows, total_columns):
    return row >= 0 and row < total_rows and column >= 0 and column < total_columns

def print_diagonal(row, column, matrix):
    diag_string = ""
    while authorize(row, column, len(matrix), len(matrix[0])):
        diag_string += str(matrix[row][column])
        row -= 1
        column += 1
    print diag_string

def print_diagonals(matrix):
    for row in range(len(matrix)):
        print_diagonal(row, 0, matrix)
    for col in range(1, len(matrix[0])):
        print_diagonal(len(matrix) - 1, col, matrix)

matrix = [[9,8,7,6,5],
          [0,1,2,3,4],
          [5,5,5,5,5]]

print_diagonals(matrix)
