# A tree is a hierarchical data structure with a root node and branches representing sub-trees.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left:
                self._insert(value, current_node.left)
            else:
                current_node.left = TreeNode(value)
        else:
            if current_node.right:
                self._insert(value, current_node.right)
            else:
                current_node.right = TreeNode(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, current_node):
        if not current_node:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)

    def delete(self, value):
        self.root = self._delete(value, self.root)

    def _delete(self, value, current_node):
        if not current_node:
            return current_node
        if value < current_node.value:
            current_node.left = self._delete(value, current_node.left)
        elif value > current_node.value:
            current_node.right = self._delete(value, current_node.right)
        else:
            # Node with one child or no child
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            # Node with two children
            current_node.value = self._min_value_node(current_node.right).value
            current_node.right = self._delete(current_node.value, current_node.right)
        return current_node

    def _min_value_node(self, node):
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def display(self):
        self._display(self.root, 0)

    def _display(self, node, level):
        if node:
            self._display(node.right, level + 1)
            print("  " * level + str(node.value))
            self._display(node.left, level + 1)

# Using the binary tree
binary_tree = BinaryTree()
binary_tree.insert(5)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.display()

binary_tree.delete(3)
binary_tree.display()
print(binary_tree.search(7))
