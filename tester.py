def find_duplicates(listy):
    duplicates_list = []
    d = {}
    for item in listy:
        d[item] = d.get(item, 0) + 1
    keys = d.keys()
    for key in keys:
        if d[key] > 1:
            duplicates_list.append(key)
    print duplicates_list


votesToGoEatCake = [True, True, True, True]
hackbrightStudents = ["katie", "amy", "jenny", "katie", "kelley", "katie", "amy"]
classroomIds = [47, 12, 19, 22, 26, 99, 30, 50, 324, 003, 44, 33, 346, 354, 44, 235, 45, 34, 44, 590, 9, 99, 0, 1, 3, 33, 999, 9]
randomJunkIFound = ["katie", "True", True, 19, "gargoyles", "!", 2 + 3, "2 + 3", 19, "19", 19 == "19", 6, False, False]


find_duplicates(votesToGoEatCake)
find_duplicates(hackbrightStudents)
find_duplicates(classroomIds)
find_duplicates(randomJunkIFound)