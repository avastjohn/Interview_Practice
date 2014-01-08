"""
Given a sorted array of strings which is interspersed with empty strings,
write a method to find the location of a given string
return position of string in the array or return -1 if string is not found
"""

def find_string(list_of_strings, target):
    for i in range(len(list_of_strings)):
        if list_of_strings[i] == target:
            return i
    return -1

list1 = ["", "", "turd", "", "", "", "", "", "poopy"]
list2 = ["", "", "john", "", "is", "", "", "a", "poopy", "face"]

print find_string(list1, "turd")
print find_string(list2, "turd")