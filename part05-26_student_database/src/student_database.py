def add_student(students: dict, name: str):
    if name not in students:
        variavel = ["no completed courses"]
        students[name] = variavel
    
    
            
    
def add_course(students: dict, name: str, completion: tuple):
    if name in students:
        if "no completed courses" in students[name]:
            students[name] = []
        students[name].append(completion) 
    else:
        print(f"{name}: no such person in the database")



def print_student(students: dict, name: str):
    num = 0
    counter = 0
    course = ""
    credit = 0
    if name in students:
        print(f"{name}: ")
        for i in students[name]:
            counter += 1
            values = students[name]
            if len(values) > 1:
                course, credit = i
                num += credit
                print(f" {course} {credit}")
                print(f"average grade {num/counter}")
            elif len(values) <= 1:
                print(" no completed courses")
    elif name not in students:
        print(f"{name}: no such person in the database")    
    
    
    
    
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    print_student(students, "Peter")






