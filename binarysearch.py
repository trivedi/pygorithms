class Node:
    left = None
    right = None
    def __init__(self, key, val):
        self.key = key
        self.val = val

def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    elif key < node.key:
        node.left = insert(node.left, key, val)
    else:
        node.right = insert(node.right, key, val)
    return node

def search(node, key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node.val
    elif key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)

class Tree:
    """Implements a binary search tree with complexity of O(logn)
       Usage: >>> tree = Tree()
              >>> tree["a"] = 42
              >>> "a" in tree
              True
              >>> "b" in tree
              False
    """
    root = None
    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)
    def __getitem__(self, key):
        return search(self.root, key)
    def __contains__(self, key):
        try:
            search(self.root, key)
        except KeyError:
            return False
        return True
