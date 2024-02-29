def block_correct(sudoku: list, row_no: int, column_no: int):


        # Extract the column from the Sudoku grid
    # column = [row[column_no] for row in sudoku]
    
    # # Check if the column contains each of the numbers 1 to 9 at most once
    # for number in range(1, 10):
    #     if column.count(number) > 1:
    #         return False
    # return True


    # row = sudoku[row_no]
    # for num in range(1, 10):  # Numbers in Sudoku are from 1 to 9
    #     if row.count(num) > 1:
    #         return False
    # return True
    counter = 0
    counter3 = 0
    new_list = []
    while len(new_list) < 9:
        num = sudoku[int(row_no) + counter][ int(column_no) + counter3]
        new_list.append(num)
        counter3 += 1
        if counter3 == 3:
            counter3 = 0
            counter += 1
    for num in range(1, 10):  # Numbers in Sudoku are from 1 to 9
        if new_list.count(num) > 1:
            return False
    return True


if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 0))