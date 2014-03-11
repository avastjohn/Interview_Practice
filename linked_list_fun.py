class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.head = None


    def print_list(self):
        current = self.head
        linky = []
        while current.next:
            linky.append(current.data)
            current = current.next
        linky.append(current.data)
        print linky

    def reverse_linked_list(self):
        previous = self.head
        current = previous.next
        temp = current.next
        while current.next.next:
            current.next = previous
            previous = current
            current = temp
            temp = temp.next
        current.next = previous
        temp.next = current
        self.head.next = None
        self.head = temp



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

abdomen.print_list()
abdomen.reverse_linked_list()
abdomen.print_list()
