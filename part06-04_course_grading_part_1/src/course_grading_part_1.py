if True:
    
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    

names = {}

with open(student_info) as new_file:
    nome_completo = []
    counter = 0
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        else:
            for i in parts:
                if "123" in i:
                    continue
                else:
                    nome_completo.append(i)
                    counter += 1
                    if counter == 2:
                        separator = " "
                        result_string = separator.join(nome_completo)
                        names[result_string] = None
                        nome_completo = []
                        result_string = ""
                        counter = 0      

                
                 
salaries = []
with open(exercise_data) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        else:
            suma1 = 0 
            for i in parts:
                if "123" in i:
                    continue
                else:
                    i = int(i)
                    suma1 += i
            salaries.append(suma1)       


counter = 0
for key, values in names.items() :
    print(key, salaries[counter])
    counter +=1
    