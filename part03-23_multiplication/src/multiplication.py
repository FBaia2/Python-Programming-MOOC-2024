number = int(input("Please type in a number: "))
attempts = 0
var1 = 1
var2 = 1

while var1 <= number and var2 <= number:
    
    print(f"{var1} x {var2} = {var1*var2}")

    attempts +=1
    var2 +=1

    if var2 == number+1:
        var2 = 1

    if attempts == number:
        var1 +=1
        attempts = 0

