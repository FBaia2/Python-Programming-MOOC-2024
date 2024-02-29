def transpose(matrix: list):
    # Get the size of the matrix
    size = len(matrix)

    # Create a new matrix with the same size
    transposed_matrix = []
    for i in range(size):
        # Create a new row
        new_row = []
        for j in range(size):
            # Add the transposed element to the new row
            new_row.append(matrix[j][i])
        # Add the new row to the transposed matrix
        transposed_matrix.append(new_row)

    # Replace the original matrix with the transposed one
    matrix[:] = transposed_matrix

if __name__ == "__main__":
    matrix1 = [[1, 2],
               [4, 5]]
    transpose(matrix1)
    print(matrix1)
