def new_person(name: str, age: int):
    # Check if name is an empty string
    if not name:
        raise ValueError("Name cannot be an empty string.")
    # Check if name contains less than two words
    if len(name.split()) < 2:
        raise ValueError("Name must contain at least two words.")
    # Check if name is longer than 40 characters
    if len(name) > 40:
        raise ValueError("Name cannot be longer than 40 characters.")
    # Check if age is a negative number or greater than 150
    if age < 0 or age > 150:
        raise ValueError("Age must be a positive number and less than or equal to 150.")
    # If all checks pass, return the tuple
    return (name, age)

if __name__=="__main__":
    n = new_person("Jonh deeee" , 30)
    print(n)