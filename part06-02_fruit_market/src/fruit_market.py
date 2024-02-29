def read_fruits():
    dicionario = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            grades = parts[1]
            grades = float(grades)
            format(grades, '.1f')
            dicionario[name] = grades
    return dicionario

    
    
    
    
    
    
    
    
if __name__=="__main__":
    print(read_fruits())