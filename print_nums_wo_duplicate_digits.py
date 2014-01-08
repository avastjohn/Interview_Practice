"""
Given a range x to y, print any number that doesn't contain duplicate digits
Ex: 2415 will print but 2414 will not (bc it has two 4s)
"""

def print_unique_digits(x, y):
    for num in range(x, y):
        num_str = str(num)
        d = {}
        repeats = False
        for digit in num_str:
            if d.get(digit):
                repeats = True
                break
            else:
                d[digit] = True
        if not repeats:
            print num


x = 10
y = 5000

print_unique_digits(x, y)