class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, node):
        """Insert Node class instance in BST.

        If node with same key is in tree, element not will be added.

        :param node: Node class instance
        :return: None
        """
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

    def delete(self, node):
        """Delete existing in BST node.

        Three cases are possible:
        1) node not have child
        2) node have 1 child
        3) node have 2 children

        :param node: Node class instance
        :return: None
        """
        if not node.left:
            self.transplant(node, node.right)
        elif not node.right:
            self.transplant(node, node.left)
        else:
            successor = BST.find_successor(node)
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def transplant(self, node, subtree_root):
        """Function to transplant subtree of inner root to parent.

        :param node: deleting node
        :param subtree_root: node that take place of node root
        :return:
        """
        if not node.parent:
            self.root = subtree_root
        elif node.parent.left == node:
            node.parent.left = subtree_root
        else:
            node.parent.right = subtree_root
        if subtree_root:
            subtree_root.parent = node.parent

    def __contains__(self, key):
        raise NotImplementedError

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    @staticmethod
    def print_inorder(root):
        """Walks through the tree and prints the nodes in ascending order.

        :param root: link to the root
        :return: None
        """
        if root:
            BST.print_inorder(root.left)
            print(root.key)
            BST.print_inorder(root.right)

    @staticmethod
    def search(root, key):
        if root is None or key == root.key:
            return root
        if key < root.key:
            return BST.search(root.left, key)
        else:
            return BST.search(root.right, key)

    @staticmethod
    def search_iterative(root, key):
        while root is not None and root.key != key:
            if key < root.key:
                root = root.left
            else:
                root = root.right
        return root

    @staticmethod
    def find_minimum(root):
        while root.left is not None:
            root = root.left
        return root

    @staticmethod
    def find_maximum(root):
        while root.right is not None:
            root = root.right
        return root

    @staticmethod
    def find_successor(node):
        if node.right is not None:
            return BST.find_minimum(node.right)
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = node.parent
        return parent

    @staticmethod
    def find_predecessor(node):
        if node.left:
            return BST.find_maximum(node.left)
        parent = node.parent
        while parent and parent.left == node:
            node = parent
            parent = node.parent

    def __iter__(self):
        return self.root.__iter__()
