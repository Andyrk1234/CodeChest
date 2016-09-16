__author__ = 'Paarth Bhasin'


def heap_sort(A, print_flag):
    heapify(A, len(A))

    # flatten heap into sorted array
    length = len(A) - 1
    j = 1
    for i in range(length, 0, -1):
        #print("A[i]= " + str(A[i]))
        if print_flag:
            print(A[j:])
            j+=1
        if A[1] < A[i]:

            #print(A[1])
            #print(A[i])
            swap(A, 1, i)
            #print("Here: " + str(A))
            moveDown(A, 1, i - 1)

            # print(A)


def moveDown(aList, first, last):
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if (largest < last) and (aList[largest] < aList[largest + 1]):
            largest += 1

        # right child is larger than parent
        if aList[largest] > aList[first]:
            swap(aList, largest, first)
            # move down to largest child
            first = largest
            largest = 2 * first + 1
        else:
            return  # force exit


def delete_max(A, n):
    swap(A, 1, n - 1)
    moveDown(A, 1, n - 2)
    print(A[: n - 1])

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def heapify(A, n):
    # convert aList to heap
    # print(A[n - 1])
    A.append(A[n - 1])
    for i in range(len(A) - 2, 0, -1):
        A[i] = A[i - 1]
    A[0] = None
    print("Here: ")
    print(A)


def main():
    A = []

    f = open("numbers.txt", 'r')
    lines = f.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            A.append(word)

    heap_sort(A, True)
    # print(A)
    # delete_max(A, len(A))
    print(A)


if __name__ == "__main__":
    main()
