from datetime import date

def is_it_valid(pic: str):
    picnic = [i for i in pic]
    year = ''
    if picnic[6] == "-":
        year =  "19" + ''.join(picnic[4:6])
    elif picnic[6] == "+":
        year =  "18" + ''.join(picnic[4:6])
    elif picnic[6] == "A":
        year =  "20" + ''.join(picnic[4:6])
    
    day = ''.join(picnic[:2])
    month = ''.join(picnic[2:4])
    day1 = int(day)
    month1 = int(month)
    year1 = int(year)
    ninedigit = ''.join(picnic[:6]) + ''.join(picnic[7:10])
    ninedigit = int(ninedigit)
    remainder = ninedigit % 31
    strong = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    strong = [i for i in strong]
    if strong[remainder] == picnic[-1] and len(picnic) == 11:
        try:
            date(year1, month1, day1)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
