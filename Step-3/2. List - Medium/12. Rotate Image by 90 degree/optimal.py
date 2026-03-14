def rotateMatrixClockwise(matrix):
    n = len(matrix)

    # transpose
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    # reverse every row
    for i in range(n):
        matrix[i].reverse()

    return matrix

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    ans = rotateMatrixClockwise(matrix)
    print(ans)

"""
Time Complexity - For transpose - O(N*N) and reverse - O(N*N) ~~ O(N^2)
Space Complexity - O(1)
"""