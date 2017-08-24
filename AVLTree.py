__author__ = 'Paarth Bhasin' # FIT2004

class avlnode(object):
    """
    A node in an avl tree.
    """

    def __init__(self, item):
        "Construct."

        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        "String representation."
        return str(self.item)

    def __repr__(self):
        "String representation."
        return str(self.item)

class avltree(object):
    """
    An avl tree.
    """

    def __init__(self):
        "Construct."
        self.node = None
        self.height = -1
        self.balance = 0

    def __contains__(self, item):
        return self.search_avl(self.node, item, "")

    def search_avl(self, current, item, path):
        # print("Node: ", end=" ")
        # print(current)
        if current is None:
            print("?HYtjjugtjutjut")
            raise KeyError("key not found")
        elif int(item) == int(current.item):
            print(current.item)
            path += str(current.item)
            print("True")
            return path
        elif int(item) < int(current.item):
            path += str(current.item) + "-> "
            return self.search_avl(current.left, item, path)

        else:  # key > current.key
            path += str(current.item) + "-> "
            print("?")
            return self.search_avl(current.right, item, path)

    def insert(self, item):
        """
        Insert new key into node
        """
        n = avlnode(item)

        if not self.node:
            self.node = n
            self.node.left = avltree()
            self.node.right = avltree()
        elif item < self.node.item:
            self.node.left.insert(item)
        elif item > self.node.item:
            self.node.right.insert(item)

        self.rebalance()

    def rebalance(self):
        """
        Rebalance tree. After inserting or deleting a node,
        it is necessary to check each of the node's ancestors for consistency with the rules of AVL
        """

        self.update_heights(recursive=False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            # Left subtree is larger than right subtree
            if self.balance > 1:

                # Left Right Case -> rotate y,z to the left
                if self.node.left.balance < 0:

                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:

                if self.node.right.balance > 0:

                    self.node.right.rotate_right()
                    self.update_balances()

                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        """
        Update tree height

        Tree height is max height of either left or right subtrees +1 for root of the tree
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()

            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else:
            self.height = -1

    def update_balances(self, recursive=True):
        """
        Calculate tree balance factor

        The balance factor is calculated as follows:
            balance = height(left subtree) - height(right subtree).
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rotate_right(self):
        """
        Right rotation
            set self as the right subtree of left subtree
        """
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        """
        Left rotation
            set self as the left subtree of right subtree
        """
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def print_inorder(self):
        self.print_inorder_aux(self.node)

    def print_inorder_aux(self, current):
        if current is not None:  # if not a base case
            self.print_inorder_aux(current.left)
            print(current.item)
            self.print_inorder_aux(current.right)
        else:
            print(current)


def main():
    quit = False

    avl = avltree()
    f = open("numbers.txt", 'r')
    lines = f.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            avl.insert(word)

        item = int(input("Enter item you want to look for: "))
        avl.__contains__(item)

if __name__ == "__main__":
    main()
