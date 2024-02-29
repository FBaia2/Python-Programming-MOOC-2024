


def search_by_name(filename: str, word: str):
    primeira = []
    dicionario = {}
    ingredients = []
    save_key = ""
    counter = 0
    with open(filename) as new_file:
        list_content = new_file.read().split("\n")
        for line in list_content:
            if line != line.lower():
                dicionario[line] = None
                save_key = line
            elif line.isdigit() == True:
                dicionario[save_key] = line
                counter = 0
            elif line.isdigit() == False:
                save_key = line
                ingredients.append(line)
    for i in dicionario:
        if word.lower() in i.lower():
            primeira.append(i)
    return primeira

    
    
# def search_by_time(filename: str, prep_time: int):
#     quarta = []
#     segunda = []
#     terceira = []
#     primeira = []
#     dicionario = {}
#     ingredients = []
#     save_key = ""
#     counter = 0
#     with open(filename) as new_file:
#         list_content = new_file.read().split("\n")
#         for line in list_content:
#             if line != line.lower():
#                 dicionario[line] = None
#                 save_key = line
#             elif line.isdigit() == True:
#                 dicionario[save_key] = line
#                 counter = 0
#             elif line.isdigit() == False:
#                 save_key = line
#                 ingredients.append(line)
#     for i in dicionario:
#         numpi = int(dicionario[i])
#         if numpi <= prep_time:
#             segunda.append(i)
#             terceira.append(dicionario[i])
#     if len(segunda) == 1:
#         quarta = segunda[0] + ", preparation time " + terceira[0] + " min \n"
#         return quarta
    
def search_by_time(filename: str, prep_time: int):
    quarta = []
    segunda = []
    terceira = []
    primeira = []
    dicionario = {}
    ingredients = []
    save_key = ""
    counter = 0
    with open(filename) as new_file:
        list_content = new_file.read().split("\n")
        for line in list_content:
            if line != line.lower():
                dicionario[line] = None
                save_key = line
            elif line.isdigit() == True:
                dicionario[save_key] = line
                counter = 0
            elif line.isdigit() == False:
                save_key = line
                ingredients.append(line)
    for i in dicionario:
        numpi = int(dicionario[i])
        if numpi <= prep_time:
            segunda.append(i)
            terceira.append(dicionario[i])
    for i in range(len(segunda)):
        quarta.append(segunda[i] + ", preparation time " + terceira[i] + " min")
    return quarta



    
    
    
    
    
    
if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "lls")
    found_recipes = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)
    # print(found_recipes)
        
        
