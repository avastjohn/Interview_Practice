from math import abs


def find_bricks_that_fit(input_file):
    lines = input_file.readlines()
    for line in lines:
        line = line.split()
        # turn first set of coordinates into a list
        hole_vertex_1 = list(line[0])
        # get second set of coordinates by looking for a "]"
        for i in range(len(line[1])):
            if line[1][i] == "]":
                hole_vertex_2 = list(line[1][:i])
                break
        # subtract the x coords and the y coords from the two vertices to get 
        # width and height
        hole_size = [None, None]
        # x coordinates
        hole_size[0] = abs(hole_vertex_1[0]-hole_vertex_2[0])
        hole_size[1] = abs(hole_vertex_1[1]-hole_vertex_2[1])
