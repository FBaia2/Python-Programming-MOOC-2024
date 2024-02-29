def matrix_sum():
    suma = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            lines = line.strip().split(",")
            for num in lines:
                suma += int(num)
    return suma



def matrix_max():
    best = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            lines = line.strip().split(",")
            for num in lines:
                suma = int(num)
                if suma > best:
                    best = suma
    return best




def row_sums():
    best = 0
    numa = 0
    counter = 0
    row1 = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            lines = line.split(",")
            numa = len(lines)
            for num in lines:
                counter +=1
                best += (int(num))
                if counter == numa:
                    row1.append(best)
                    counter = 0
                    best = 0
    return row1




if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())