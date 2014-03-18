

solved = [[2,4,8,3,9,5,7,1,6],
          [5,7,1,6,2,8,3,4,9],
          [9,3,6,7,4,1,5,8,2],
          [6,8,2,5,3,9,1,7,4],
          [3,5,9,1,7,4,6,2,8],
          [7,1,4,8,6,2,9,5,3],
          [8,6,3,4,1,7,2,9,5],
          [1,9,5,2,8,6,4,3,7],
          [4,2,7,9,5,3,8,6,1],]

false_solved = [[2,4,8,3,9,5,7,1,6],
                [5,7,1,6,2,8,3,4,9],
                [9,3,6,7,4,1,5,8,2],
                [6,8,2,5,3,9,1,7,4],
                [3,5,9,1,7,4,6,2,8],
                [7,1,4,8,6,2,9,5,3],
                [8,6,3,4,1,7,2,9,5],
                [1,9,5,2,8,6,4,3,7],
                [4,2,7,9,5,3,8,1,6]]

false_solved2 = [[1,2,3,4,5,6,7,8,9],
                 [2,3,4,5,6,7,8,9,1],
                 [3,4,5,6,7,8,9,1,2],
                 [4,5,6,7,8,9,1,2,3],
                 [5,6,7,8,9,1,2,3,4],
                 [6,7,8,9,1,2,3,4,5],
                 [7,8,9,1,2,3,4,5,6],
                 [8,9,1,2,3,4,5,6,7],
                 [9,1,2,3,4,5,6,7,8]]
def check_nine(nine_list):
    d = {}
    for num in nine_list:
        if d.get(num):
            return False
        else:
            d[num] = True
    return True

def sudoku_checker(matrix):
    for i in range(9):
        #check rows
        if not check_nine(matrix[i]):
            return False
        #check collumns
        col = []
        for j in range(9):
            col.append(matrix[j][i])
        if not check_nine(col):
            return False
        #check boxes
        if i % 3 == 0:
            box1 = []
            box2 = []
            box3 = []
            for j in range(9):
                if j<3:
                    box1 += (matrix[j][i:i+3])
                elif j < 6:
                    box2 += (matrix[j][i:i+3])
                else:
                    box3 += (matrix[j][i:i+3])
            if not (check_nine(box1) and check_nine(box2) and check_nine(box3)):
                return False
    return True


print sudoku_checker(solved)
print sudoku_checker(false_solved)
print sudoku_checker(false_solved2)