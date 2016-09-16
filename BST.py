__author__ = 'Paarth Bhasin'


class BinarySearchTreeNode:
    def __init__(self, item=None, left=None, right=None):
        # self.key = key
        self.item = item
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def __setitem__(self, item):
        self.root = self.setitem_aux(self.root, item)

    def setitem_aux(self, current, item):
        if current is None:
            # base case: at the leaf
            current = BinarySearchTreeNode(item)
        elif int(item) < int(current.item):
            current.left = self.setitem_aux(current.left, item)
        elif int(item) > int(current.item):
            current.right = self.setitem_aux(current.right, item)
        else:  # item == current.item
            current.item = item

        return current

    def __contains__(self, item):
        return self.contains_aux(self.root, item, "")

    def contains_aux(self, current, item, path):
        if current is None:
            # base case: empty
            raise KeyError("key not found")
        elif int(item) == int(current.item):
            # base case: found
            path += str(current.item)
            print("True")
            return path
        elif int(item) < int(current.item):
            path += str(current.item) + "-> "
            return self.contains_aux(current.left, item, path)
        else:  # key > current.key
            path += str(current.item) + "-> "
            return self.contains_aux(current.right, item, path)

    def __search__(self, item):
        return self.search_aux(self.root, item)

    def search_aux(self, current, item):
        if current is None:
            # base case: empty
            raise KeyError("key not found")
        elif int(item) == int(current.item):
            # base case: found
            return True
        elif int(item) < int(current.item):
            return self.search_aux(current.left, item)
        else:  # key > current.key
            return self.search_aux(current.right, item)

    def print_inorder(self):
        self.print_inorder_aux(self.root)

    def print_inorder_aux(self, current):
        if current is not None:  # if not a base case
            self.print_inorder_aux(current.left)
            print(current.item)
            self.print_inorder_aux(current.right)
        else:
            print(current)
