class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def print_leaf_nodes(self):
        def _print_leaves(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                print(node.key)
            _print_leaves(node.left)
            _print_leaves(node.right)

        print("Leaf nodes:")
        _print_leaves(self.root)
