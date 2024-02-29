if True:
    
    student_info = input("Student information: ")
    exec_points = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    
    student_info = "students3.csv"
    exec_points = "exercises3.csv"
    exam_points = "exam_points3.csv"
    
    
    
    
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
 
              
                 
e_points = []
with open(exec_points) as new_file:
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
            e_points.append(suma1)



ea_points = []
with open(exam_points) as new_file:
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
            ea_points.append(suma1)




l = []
for i in e_points:
    i = int(i)
    u = (i * 100) / 40
    if u < 10:
        l.append(0)
    elif 10 <= u < 20:
        l.append(1)
    elif 20 <= u < 30:
        l.append(2)
    elif 30 <= u < 40:
        l.append(3)
    elif 40 <= u < 50:
        l.append(4)
    elif 50 <= u < 60:
        l.append(5)
    elif 60 <= u < 70:
        l.append(6)
    elif 70 <= u < 80:
        l.append(7)
    elif 80 <= u < 90:
        l.append(8)
    elif 90 <= u < 100:
        l.append(9)
    elif u == 100:
        l.append(10)



sumer = []
sumo = 0
babs = len(ea_points)
for i in range(babs):
    x = ea_points[i]
    x = int(x)
    y = l[i]
    y = int(y)
    sumo = y + x
    sumer.append(sumo)
    sumo = 0
    

    
g = []
for i in sumer:
    i = int(i)
    if 0 <= i <= 14:
        g.append(0)
    elif 15 <= i <= 17:
        g.append(1)
    elif 18 <= i <= 20:
        g.append(2)
    elif 21 <= i <= 23:
        g.append(3)
    elif 24 <= i <= 27:
        g.append(4)
    elif 28 <= i:
        g.append(5)
        


x = 0
for i in names:
    names[i] = g[x]
    x+=1


for nome, valore in names.items():
    print(f"{nome} {valore}")
    