"""
Given sorted list of integers, create binary tree ???????????????????????????????
"""
import pdb

class Node(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def print_depth_first(self):
        if self is None:
            return
        print self.data
        print_depth_first(self.left)
        print_depth_first(self.right)

def create_tree(sorted_list):
    if sorted_list == []:
        return None
    node = Node()
    node.data = sorted_list[len(sorted_list)/2]
    node.left = create_tree(sorted_list[:len(sorted_list)/2])
    node.right = create_tree(sorted_list[(len(sorted_list)/2) + 1:])
    return node

def main():
    sorted_list = [1, 2, 3, 4, 5, 6, 7]

    my_tree=create_tree(sorted_list)

    pdb.set_trace()

main()