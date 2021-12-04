# Given a matrix of M x N elements (M rows, N columns), 
# Print all elements of the matrix in diagonal order in Time Complexity O(m*n) 
# and Space Complexity O(1)
def diagonalPrint(matrix, r, c):

    for k in range(0, r):
        i = k
        j = 0
        while (i >= 0):
            print(matrix[i][j])
            i -= 1
            j += 1

    for k in range(1, c):
        i = r - 1
        j = k
        while (j <= c-1):
            print(matrix[i][j])
            i -= 1
            j += 1


matrix = [[1,   2,  3,  4,  5],
          [6,   7,  8,  9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20], ]
diagonalPrint(matrix, 4, 5)
