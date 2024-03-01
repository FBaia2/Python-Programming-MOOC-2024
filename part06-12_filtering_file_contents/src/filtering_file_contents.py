# def filter_solutions():

#     open("correct.csv", "w").close()
#     open("incorrect.csv", "w").close()


#     with open("solutions.csv") as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             parts = line.split(';')
#             partings = str(parts)


        
#             if "+" in parts[1]:
#                 part_plus =  parts[1].split("+")
#                 partplus0 = int(part_plus[0])
#                 partplus1 = int(part_plus[1])
#                 parts2 = int(parts[2])
#                 if (partplus0 + partplus1) == parts2:
#                     with open("correct.csv", "a") as my_file:
#                         my_file.write(';'.join([str(partplus0), '+', str(partplus1), '=', str(parts2)]))
#                         my_file.write("\n")
#                 elif (partplus0 + partplus1) != parts2:
#                     with open("incorrect.csv", "a") as the_file:
#                         the_file.write(';'.join([str(partplus0), '+', str(partplus1), '=', str(parts2)]))
#                         the_file.write("\n")



#             elif "-" in parts[1]:
#                 part_minus =  parts[1].split("-")
#                 partminus0 = int(part_minus[0])
#                 partminus1 = int(part_minus[1])
#                 parts2 = int(parts[2])
#                 if (partminus0 - partminus1) == parts2:
#                     with open("correct.csv", "a") as my_file:
#                         my_file.write(';'.join([str(partminus0), '-', str(partminus1), '=', str(parts2)]))
#                         my_file.write("\n")
#                 elif (partminus0 - partminus1) != parts2:
#                     with open("incorrect.csv", "a") as the_file:
#                         the_file.write(';'.join([str(partminus0), '-', str(partminus1), '=', str(parts2)]))
#                         the_file.write("\n")

        
# if __name__ =="__main__":
#     filter_solutions()

def filter_solutions():
    # Clear the contents of the files
    open("correct.csv", "w").close()
    open("incorrect.csv", "w").close()

    with open("solutions.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(';')
            if "+" in parts[1]:
                part_plus = parts[1].split("+")
                partplus0 = int(part_plus[0])
                partplus1 = int(part_plus[1])
                parts2 = int(parts[2])
                if (partplus0 + partplus1) == parts2:
                    with open("correct.csv", "a") as my_file:
                        my_file.write(line + "\n")
                else:
                    with open("incorrect.csv", "a") as the_file:
                        the_file.write(line + "\n")
            elif "-" in parts[1]:
                part_minus = parts[1].split("-")
                partminus0 = int(part_minus[0])
                partminus1 = int(part_minus[1])
                parts2 = int(parts[2])
                if (partminus0 - partminus1) == parts2:
                    with open("correct.csv", "a") as my_file:
                        my_file.write(line + "\n")
                else:
                    with open("incorrect.csv", "a") as the_file:
                        the_file.write(line + "\n")

if __name__ =="__main__":
    filter_solutions()
