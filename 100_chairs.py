
"""
You are in a room with a circle of 100 chairs. The chairs are numbered sequentially from 1 to 100.
At some point in time, the person in chair 1 will be asked to leave. The person in chair 2 will be 
skipped, and the person in chair 3 will be asked to leave. This pattern of skipping one person and 
asking the next to leave will keep going around the circle until there is one person left - the survivor.
Write a program to determine which chair the survivor is sitting in.
"""
def find_next_occupied_chair(chairs, which_chair):
    which_chair += 1
    which_chair = which_chair % len(chairs) 
    while not chairs[which_chair]:
        which_chair += 1
        which_chair = which_chair % len(chairs)     
    return which_chair

def go_through_chairs(num_of_chairs):
    chairs = [True]*num_of_chairs
    chairs_removed = 0
    need_to_skip = False
    which_chair = -1
    while chairs_removed < len(chairs) -1:
    # until only one chair remians:

        if need_to_skip:
            which_chair = find_next_occupied_chair(chairs, which_chair)
            need_to_skip = False

        else:
            which_chair = find_next_occupied_chair(chairs, which_chair)
            chairs[which_chair] = False
            chairs_removed += 1
            need_to_skip = True
    for i in range(len(chairs)):
        if chairs[i]:
            return "Last chair occupied is #" + str(i + 1)


print go_through_chairs(100)