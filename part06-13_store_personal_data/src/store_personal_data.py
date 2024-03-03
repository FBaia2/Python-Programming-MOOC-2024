def store_personal_data(person: tuple):
    with open("people.csv", "a") as my_file:
        people0 = str(person[0])
        people1 = str(person[1])
        people2 = str(person[2])
        people = people0 + ";" + people1 + ";" + people2
        my_file.write(people)
        my_file.write("\n")





if __name__=="__main__":
    person_data = ("Paul Paulson", 37, 175.5)  # This is a tuple
    store_personal_data(person_data)
