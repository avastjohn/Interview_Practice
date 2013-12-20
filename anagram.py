# Check if two strings are anagrams

str_1 = "do have salami snot"
str_2 = "Thomas Alva Edison"

def anagram_checker(str_1, str_2):
    # make lowercase, delete white space, find whether are anagrams of each other
    new_1 = str_1.lower().replace(" ", "")
    new_2 = str_2.lower().replace(" ", "")
    dict_1 = {}
    dict_2 = {}
    for char in new_1:
        dict_1[char] = dict_1.get(char, 0) + 1
    for char in new_2:
        dict_2[char] = dict_2.get(char, 0) + 1

    return dict_1 == dict_2


print anagram_checker(str_1, str_2)