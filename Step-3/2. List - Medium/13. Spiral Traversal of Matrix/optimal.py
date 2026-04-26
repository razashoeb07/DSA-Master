def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    top, left = 0,0
    bottom = len(matrix)-1 # last row index
    right = len(matrix[0])-1 # last column index
    result = []

    # traverse the matrix until the these condition true
    while top <= bottom and left <= right:

        # move left to right across the top rows
        for i in range(left,right + 1):
            result.append(matrix[top][i])

        top += 1

        # move top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])

        right -= 1

        # move right to left if rows still valid
        if top <= bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])

            bottom -= 1

        # move bottom to top - if roes still valid
        if left <= right:
            for i in range(bottom, top-1,-1):
                result.append(matrix[i][left])

            left += 1
    return result

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ans = spiralOrder(matrix)
    print(ans)

"""
Time Complexity: O(m × n),Because we visit each element of the matrix exactly once, where `m` is the number 
                of rows and `n` is the number of columns.

Space Complexity: 
O(1)We use only a few integer variables to keep track of boundaries (top, bottom, left, right).
"""