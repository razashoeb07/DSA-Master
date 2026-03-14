from mpl_toolkits.mplot3d.art3d import rotate_axes


def rotateMatrixClockwise(matrix):
    n = len(matrix)
    rotate = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotate[j][n-i-1] = matrix[i][j]

    return rotate


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans = rotateMatrixClockwise(matrix)
    print(ans)

"""
Time Complexity - O(N^2)
Space Complexity - O(N^2)
"""