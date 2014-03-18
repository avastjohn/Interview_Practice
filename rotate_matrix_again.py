def rotate_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[-j-1][i])
        new_matrix.append(new_row)
    return new_matrix

matrix = [[1,2,3,4],[5,6,7,8],[9,0,1,2]]

new = rotate_matrix(matrix)
for row in new:
    print row