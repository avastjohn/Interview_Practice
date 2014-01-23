"""
Given a positive integer x, return the sum of all integers from 0 to x that are multiples of 3 and/or 5
"""


def get_sum(x):
    x-=1
    return (((x//3)*(3+x-(x%3)))+((x//5)*(5+x-(x%5)))-((x//15)*(15+x-(x%15))))/2



x = 1000
print get_sum(x)
