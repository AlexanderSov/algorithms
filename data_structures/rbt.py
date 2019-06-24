class RBNode:
    """Class for creating node or rb tree.

    0 - red node,
    1 - black tree
    """
    def __init__(self, key, color=0, parent=None, left=None,
                 right=None):
        self.color = color
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class RBTree:
    def __init__(self, root):
        self.root = root

    def rotate_left(self, node):
        """Execute left rotate for node.

        Tree example:              After:
                 root               root
                   \\                  \\
                   node                right
                  |    \\              ||  \\
                  x    right         node  right2
                       ||   \\       || \\
                      left  right2   x  left
        """
        right = node.right
        if right is None:
            return
        # transplant left subtree of right node in node
        node.right = right.left
        if right.left:
            right.left.parent = node
        # check parent and set in parent link to right
        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node.parent.left == node:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    def rotate_right(self, node):
        left = node.left
        if left is None:
            return
        node.left = left.right
        if left.right:
            left.right.parent = node
        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node.parent.left == node:
            node.parent.left = left
        else:
            node.parent.right = left
        left.right = node
        node.parent = left

    def insert(self, node):
        parent = None
        tree_node = self.root
        while tree_node:
            parent = tree_node
            if node.key < tree_node.key:
                tree_node = tree_node.left
            elif node.key > tree_node.key:
                tree_node = tree_node.right
            else:
                return
        node.parent = parent
        if not parent:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        # difference between BST insert
        node.left, node.right = None, None
        self.fix_insert(node)

    def fix_insert(self, node):
        pass
