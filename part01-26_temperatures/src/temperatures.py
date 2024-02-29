# Write your solution here
tempF = float(input("Please type in a temperature (F):"))
conversionToC = float(tempF - 32) * 5/9 
if conversionToC < 0:
    print(f"{tempF} degrees Fahrenheit equals {conversionToC} degrees Celsius")
    print("Brr! It's cold in here!")
else:
    print(f"{tempF} degrees Fahrenheit equals {conversionToC} degrees Celsius")