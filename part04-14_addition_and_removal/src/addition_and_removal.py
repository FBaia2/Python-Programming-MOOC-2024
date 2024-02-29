# Write your solution here

# my_list = []
# inputing = input("a(d)d, (r)emove or e(x)it: ")
# while inputing != "x":    
#     if inputing == "d" and len(my_listlist) == 0:
#         inputing = input("a(d)d, (r)emove or e(x)it: ")
#         my_list.append(1)
#         elif inputing == "d" and len(my_list) != 0:
#             longth = len(my_list)
        
    
#     if inputing == "r":
#         inputing = input("a(d)d, (r)emove or e(x)it: ")

#     print(my_list)

print("The list is now []")
my_list = []
inputing = input("a(d)d, (r)emove or e(x)it: ")
while inputing != "x":
    if inputing == "d" and len(my_list) == 0:
         my_list.append(1)
         print(f"The list is now {my_list}")
         inputing = input("a(d)d, (r)emove or e(x)it: ")

    if inputing == "d" and len(my_list) != 0:
         i = len(my_list)
         my_list.append(i+1)
         print(f"The list is now {my_list}")
         inputing = input("a(d)d, (r)emove or e(x)it: ")

    if inputing == "r":
        i = len(my_list)
        my_list.remove(i)
        print(f"The list is now {my_list}")
        inputing = input("a(d)d, (r)emove or e(x)it: ")

print("Bye!")
         