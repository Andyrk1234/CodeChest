__author__ = 'Paarth Bhasin'


def UnionByCount(lines):
    count = 0
    # nodes = 0
    time1 = 0
    tree = []
    for line in lines:
        print(count)
        print(line)
        if count == 0:
            size = int(line)
            tree = [-1] * size
            count += 1

        elif count > 0:
            count += 1
            words = line.split()
            if words[0] == "union":
                element1 = int(words[1])
                element2 = int(words[2])
                tree = union(element1, element2, tree)

            elif words[0] == "find":
                element = int(words[1])
                time1 += find_count(element - 1, tree)
        print(tree)

    return time1


def UnionByCountPathCompression(lines):
    count = 0
    # nodes = 0
    time2 = 0
    tree = []
    for line in lines:

        if count == 0:
            size = int(line) - 1
            tree = [-1] * size
            count += 1

        elif count > 0:
            count += 1
            words = line.split()
            if words[0] == "union":
                element1 = int(words[1])
                element2 = int(words[2])
                tree = union(element1, element2, tree)

            elif words[0] == "find":
                element = int(words[1])
                findPathCompression(element, tree)
                time2 += find_count(element, tree)

    return time2


def union(a, b, A):
    root1 = find(a - 1, A)
    root2 = find(b - 1, A)

    if abs(root1) == abs(root2):
        if root1 == -1:
            A[b - 1] = a - 1
            A[a - 1] -= 1

        return A

    elif abs(root1) > abs(root2):
        # root1 -= 1
        A[b - 1] = a - 1
        A[a - 1] -= 1
        return A

    else:
        # root2 -= 1
        A[a - 1] = b - 1
        A[b - 1] -= 1
        return A


def find(x, A):
    # print(x)
    if A[x] < 0:
        return A[x]
    else:
        return find(A[x], A)


def find_count(x, A, count=0):
    # print(x)
    if A[x] < 0:
        count += 1
        return count
    else:
        return find_count(A[x], A, count + 1)


def findPathCompression(x, A):
    if A[x] < 0:
        return x
    else:
        A[x] = findPathCompression(A[x], A)


def main():
    f = open("input.txt", 'r')
    lines = f.readlines()
    time1 = UnionByCount(lines)
    print("next")
    time2 = UnionByCountPathCompression(lines)
    print("Time without Path Compression: " + str(time1))
    print("Time with Path Compression: " + str(time2))


if __name__ == "__main__":
    main()
