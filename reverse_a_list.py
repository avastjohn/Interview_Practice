"""Reverse a list in place"""


def reverse_list(listy):
    for i in range(len(listy)/2):
        temp = listy[i]
        listy[i] = listy[-1 -i]
        listy[-1 -i] = temp
    return listy

listy = [1, 2, 3, 4, 5, 6, 7]
listo = [5, 6, 7, 8]

print reverse_list(listy)
print reverse_list(listo)