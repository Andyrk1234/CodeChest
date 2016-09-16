__author__ = 'Paarth Bhasin'


class NQueensBT:
    def __init__(self, N):
        self.N = N
        self.solution = [[0 for x in range(self.N)] for x in range(self.N)]

    '''def NQueensBT(N):

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                solution[i][j] = 0'''

    def solve(self, N):

        if self.placeQueens(0, N):
            Solution = []
            # print the result
            for i in range(0, N):
                for j in range(0, N):
                    print(str(self.solution[i][j]), end=" ")
                    if self.solution[i][j] == 1:
                        Solution.append(j)
                print("")

            print("{", end="")

            for i in range(len(Solution) - 1):
                print(str(Solution[i]) + ',', end=" ")
            print(str(Solution[len(Solution) - 1]) + "}")

        else:
            print("No solution exists" + '\n')

    def placeQueens(self, queen, N):
        # will place the Queens one at a time, for column wise
        # print("Queen: " + str(queen))
        if queen == N:
            # if we are here that means we have solved the problem
            return True

        for row in range(0, N):
            # check if queen can be placed row,col
            if self.canPlace(self.solution, row, queen):
                # place the queen
                self.solution[row][queen] = 1
                # solve  for next queen
                if self.placeQueens(queen + 1, N):
                    return True

                # if we are here that means above placement didn't work
                # BACKTRACK
                self.solution[row][queen] = 0

        # if we are here that means we haven't found solution
        return False

    # check if queen can be placed at matrix[row][column]
    def canPlace(self, matrix, row, column):
        # since we are filling one column at a time,
        # we will check if no queen is placed in that particular row
        for i in range(0, self.N):
            if matrix[row][i] == 1:
                return False
        # we are filling one column at a time,so we need to check the upper and
        # lower diagonal as well
        # check right upper diagonal
        # for (int i = row, j = column; i >= 0 && j >= 0; i--, j--)
        for i, j in zip(range(row - 1, -1, -1), range(column - 1, -1, -1)):
            # print("first")
            # print("i: " + str(i))
            # print("j: " + str(j), end="\n\n")
            if matrix[i][j] == 1:
                return False

        # check left lower diagonal
        # for i = row, j = column; i < matrix.length && j >= 0; i++, j--)
        for i, j in zip(range(row + 1, len(matrix)), range(column - 1, -1, -1)):
            # print("second")
            # print("i: " + str(i))
            # print("j: " + str(j), end="\n\n")
            if matrix[i][j] == 1:
                return False
        # check right lower diagonal
        # for i = row + 1, j = column + 1; i < matrix.length && j < matrix.length; i++, j++)
        for i, j in zip(range(row + 1, len(matrix)), range(column + 1, len(matrix))):
            # print("third")
            # print("i: " + str(i))
            # print("j: " + str(j), end="\n\n")
            if matrix[i][j] == 1:
                return False
        # check left upper diagonal
        # for i = row - 1, j = column + 1; i >= 0 && j < matrix.length; i--, j++)
        for i, j in zip(range(row - 1, -1, -1), range(column + 1, len(matrix))):
            # print("fourth")
            # print("i: " + str(i))
            # print("j: " + str(j), end="\n\n")
            if matrix[i][j] == 1:
                return False

        # if we are here that means we are safe to place Queen at row,column
        return True


def main():
    N = int(input("Enter order of the chess board: "))
    q = NQueensBT(N)
    q.solve(N)


if __name__ == "__main__":
    main()
