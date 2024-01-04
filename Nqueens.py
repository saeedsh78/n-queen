# A function to check if placing a queen at position (r, c) is safe
def isSafe(mat, r, c):
    # Check if there is a queen in the same column
    for i in range(r):
        if mat[i][c] == 'Q':
            return False

    # Check if there is a queen in the diagonal to the top-left
    i, j = r, c
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the diagonal to the top-right
    i, j = r, c
    while i >= 0 and j < N:
        if mat[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


# A function to print the chessboard with queens placed
def printSolution(mat):
    for i in range(N):
        print(mat[i])
    print()


# A recursive function to solve the N-Queens problem
def nQueen(mat, r):
    # If all queens are placed successfully, print the solution
    if r == N:
        print('Solution =')
        printSolution(mat)
        return

    # Try placing a queen in each column of the current row
    for i in range(N):
        # If placing a queen at (r, i) is safe, proceed
        if isSafe(mat, r, i):
            mat[r][i] = 'Q'

            # Recur for the next row
            nQueen(mat, r + 1)

            # Backtrack and remove the queen from the current position
            mat[r][i] = '–'


if __name__ == '__main__':
    # Number of queens
    N = 4

    # Chessboard represented by `mat[][]` to store the positions of queens
    mat = [['–' for x in range(N)] for y in range(N)]

    # Call the recursive function to solve the N-Queens problem
    nQueen(mat, 0)
