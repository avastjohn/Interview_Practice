def deapth_first(node):
    if node == None:
        return
    print node.data
    deapth_first(node.left)
    deapth_first(node.right)

def breadth_first(node):
    queue = [node]
    while queue:
        n = queue.pop(0)
        print n
        if n.left:
            queue.append(n.left)
        if n.right
            queue.append(n.right)