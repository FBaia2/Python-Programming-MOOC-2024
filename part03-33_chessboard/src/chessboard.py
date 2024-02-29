# # Write your solution here
# def chessboard(y):
#     attempt = 0
#     cycle1 = 0
#     if attempt % 2 == 0:
#         while attempt < y:
#             cycle1 = 0
#             attempt +=1
#             print("\n")
#             while cycle1 < y:
#                 cycle1 += 1
#                 print("1", end='')
#                 if cycle1 < y:
#                     cycle1 += 1
#                     print("0", end='')
#     elif attempt % 2 != 0:
#         while attempt < y:
#             cycle1 = 0
#             attempt +=1
#             print("\n")
#             while cycle1 < y:
#                 cycle1 += 1
#                 print("0", end='')
#                 if cycle1 < y:
#                     cycle1 += 1
#                     print("1", end='')

# # Testing the function
# if __name__ == "__main__":
#     chessboard(3)


def chessboard(y):
    attempt = 0
    while attempt < y:
        cycle1 = 0
        while cycle1 < y:
            if attempt % 2 == 0:
                if cycle1 % 2 == 0:
                    print("1", end='')
                else:
                    print("0", end='')
            else:
                if cycle1 % 2 == 0:
                    print("0", end='')
                else:
                    print("1", end='')
            cycle1 += 1
        print("\n", end='')
        attempt += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
