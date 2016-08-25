__author__ = 'Paarth Bhasin'

from HuffmanBinaryTree import BinaryTree
from HuffmanBinaryTree import Node

List1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
         'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
         'y': 0, 'z': 0}


def print_recursive_path(node, path=""):
    if node is None:
        return
    if node.left is None and node.right is None:
        print("Huffman code of ", end="")
        print(node.item + ": " + path)
    else:
        print_recursive_path(node.left, str(path) + "0")
        print_recursive_path(node.right, str(path) + "1")


def huffmancode():
    list = []
    name = input("Enter filename: ")
    filename = str(name) + ".txt"
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            for i in range(len(word)):
                if word[i] in List1:
                    List1[word[i]] += 1
    for key in List1:
        node = Node(key, None, None, List1[key])
        list.append(node)

    # Stack1 = Stack(len(list))
    # sorting the list containing binary trees nodes in descending order of frequency.
    for item in range(len(list) - 1, 0, -1):
        for i in range(item):
            if list[i].frequency > list[i + 1].frequency:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
    # Pushing nodes on the stack with the node with the least frequency at the top of the stack,

    '''for i in range(len(list)):
        Stack1.push(list[i])'''

    print(len(list))
    while len(list) > 1:
        tree1 = list[0]
        tree2 = list[1]
        list.__delitem__(0)
        list.__delitem__(0)
        node = Node(None, tree1, tree2, tree1.frequency + tree2.frequency)
        list.append(node)

        for item in range(len(list) - 1, 0, -1):
            for j in range(item):
                if list[j].frequency > list[j + 1].frequency:
                    temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp

    huffmantree = BinaryTree(list[0])
    print_recursive_path(huffmantree.root)


def main():
    huffmancode()


if __name__ == "__main__":
    main()
