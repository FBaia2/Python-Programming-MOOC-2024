import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = json.load(my_file)

    for person in data:
        hobbies = ', '.join(person["hobbies"])
        print(f"{person['name']} {person['age']} years ({hobbies})")

if __name__ == "__main__":
    print_persons("file1.json")
