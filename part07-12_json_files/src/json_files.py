import json
def print_persons(filename: str):
    lista = []
    counter = 0
    with open(filename) as my_file:
        data = my_file.read()
    courses = json.loads(data)
    for course in courses:
        print(course["name"], course["age"], end = "")
        print(" years", end = " ")
        for i in course["hobbies"]:
            lista.append(i)
        print("(", end= "")
        for i in lista:
            counter +=1
            print(f"{i}", end= "")
            if counter != len(lista):
                print(", ", end= "")
        print(")", end= "")
        lista = []
        print("\n")
        counter = 0
    


if __name__ =="__main__":
    print_persons("file1.json")