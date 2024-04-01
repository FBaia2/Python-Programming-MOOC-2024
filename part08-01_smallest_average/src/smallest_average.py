# def smallest_average(person1: dict, person2: dict, person3: dict):
#     p1_avg = 0
#     p2_avg = 0
#     p3_avg = 0
#     for key, value in person1.items(): 
#         if key != "name":
#             p1_avg += value
#     p1_avg = p1_avg / (len(person1) -1)
    
#     for key, value in person2.items(): 
#         if key != "name":
#             p2_avg += value
#     p2_avg = p2_avg / (len(person2) -1)
    
#     for key, value in person3.items(): 
#         if key != "name":
#             p3_avg += value
#     p3_avg = p3_avg / (len(person3) -1)
        
#     smallest = p1_avg

#     if p2_avg < smallest:
#         smallest = p2_avg
#     if p3_avg < smallest:
#         smallest = p3_avg
    
#     if smallest == p1_avg:
#         return person1
#     if smallest == p2_avg:
#         return person2
#     if smallest == p3_avg:
#         return person3
        
        
def average(person: dict):
    total = 0
    count = 0
    for key, value in person.items():
        if key != "name":
            total += value
            count += 1
    return total / count

def smallest_average(person1: dict, person2: dict, person3: dict):
    smallest = person1

    if average(person2) < average(smallest):
        smallest = person2

    if average(person3) < average(smallest):
        smallest = person3

    return smallest




            
    
if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3)) 
