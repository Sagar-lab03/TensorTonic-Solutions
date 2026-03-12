import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    
    row = len(A)
    col = len(A[0])

    temp = [n for row_ in A for n in row_]

    res = np.zeros((col, row))

    i = 0
    for x in range(row):
        for y in range(col):
            res[y][x] = temp[i]
            i += 1

    return res