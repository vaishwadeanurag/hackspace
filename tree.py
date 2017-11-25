class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right =right


def insert(root):
    left = input("left for:%s, enter left or enter for empty=" % root)
    right = input("right for:%s, enter right or enter for empty=" % root)
    if root:
        root = Node(data=root)
    else:
        return None

    if left:
        root.left = insert(left)
    if right:
        root.right = insert(right)

    return root

first_root = input("root=")
Tree = insert(first_root)
import ipdb;ipdb.set_trace()
