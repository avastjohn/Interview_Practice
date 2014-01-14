class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.head = None


    def print_backwards(self):
        current = self.head
        current.last = None
        while current.next:
            temp = current
            current = current.next
            current.last = temp
        print current.data
        while current.last:
            print current.last.data
            current = current.last

a = Node("a")
b = Node("b")
d = Node("d")
o = Node("o")
m = Node("m")
e = Node("e")
n = Node("n")
a.next = b
b.next = d
d.next = o
o.next = m
m.next = e
e.next = n

abdomen = Linked_list()
abdomen.head = a

abdomen.print_backwards()