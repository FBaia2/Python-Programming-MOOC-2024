name = input("Whom should I sign this to: ")
txt = input("Where shall I save it: ")

with open(txt, "w") as my_file:
    my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
