class Node:
    rightNode = None
    leftNode = None
    name = None

    def __init__(self, l, r, n):
        self.rightNode = r
        self.leftNode = l
        self.name = n

#            a
#           / \
#          b   e
#         /\
#        c  d   
#
# Reversed:
#            a
#           / \
#          e   b
#              /\
#             d  c   
#


tree = Node(Node(Node(None, None, "c"), Node(None, None, "d"), "b"), Node(None, None, "e"), "a")


def walk_depth_first(node):
    print("Visiting node: " + node.name)
    if node is None or (node.rightNode is None and node.leftNode is None):
        return
    if node.leftNode is not None:
        walk_depth_first(node.leftNode)
    if node.rightNode is not None:
        walk_depth_first(node.rightNode)


def walk_breadth_first(node):
    list = []
    if node is None:
        return
    list.insert(0, node)
    while len(list) > 0:
        n = list.pop()
        print("Visiting node: " + n.name)
        if n.leftNode is not None:
            list.insert(0, n.leftNode)
        if n.rightNode is not None:
            list.insert(0, n.rightNode)


def reverse_tree(node):
    if node.rightNode is None and node.leftNode is None:
        return
    leftNode = node.leftNode
    node.leftNode = node.rightNode
    node.rightNode = leftNode
    reverse_tree(node.leftNode)
    reverse_tree(node.rightNode)

print("Walk depth: ")
walk_depth_first(tree)
print("Walk breadth: ")
walk_breadth_first(tree)
reverse_tree(tree)
print("Reversed tree walk depth: ")
walk_depth_first(tree)
print("Reversed tree walk breadth: ")
walk_breadth_first(tree)
    