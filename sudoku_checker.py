

solved = [[2,4,8,3,9,5,7,1,6],
          [5,7,1,6,2,8,3,4,9],
          [9,3,6,7,4,1,5,8,2],
          [6,8,2,5,3,9,1,7,4],
          [3,5,9,1,7,4,6,2,8],
          [7,1,4,8,6,2,9,5,3],
          [8,6,3,4,1,7,2,9,5],
          [1,9,5,2,8,6,4,3,7],
          [4,2,7,9,5,3,8,6,1],]

def check_array_of_9(array):
    d = {}
    for item in array:
        if item in d:
            return False
        else:
            d[item] = True
    return True

def check_validity(solution):
    for i in range(9):
        column = []
        box1 = []
        box2 = []
        box3 = []
        print "row", i, solution[i]
        if not check_array_of_9(solution[i]):
            return False
        for j in range(9):
            column.append(solution[j][i])
            if i%3 == 0:
                if j < 3:
                    box1 += solution[j][i:i+3]
                elif j < 6:
                    box2 += solution[j][i:i+3]
                else:
                    box3 += solution[j][i:i+3]
        print "column", i, column
        if i%3 == 0:
            print "box1", i, box1
            print "box2", i, box2
            print "box3", i, box3
            valid1 = check_array_of_9(box1)
            valid2 = check_array_of_9(box2)
            valid3 = check_array_of_9(box3)
        valid4 = check_array_of_9(column)
        if not (valid1 and valid2 and valid3 and valid4):
            return False
    return True



print check_validity(solved)


