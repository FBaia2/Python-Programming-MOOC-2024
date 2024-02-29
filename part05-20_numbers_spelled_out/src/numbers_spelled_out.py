# Write your solution here
# def dict_of_numbers():
#     s = {
#     0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
#     6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
#     11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
#     15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 
#     19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 
#     50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
# }

# if len(numbers) == 2:
#     num2 = (numbers / 10) % 10
#     num1 = num - num2
#     return s[num1], "-", s[num2]
# elif len(num) == 1:
#     return s[num]


# if __name__== "__main__":
#     numbers = dict_of_numbers()
# print(numbers[2])
# print(numbers[11])
# print(numbers[45])
# print(numbers[99])
# print(numbers[0])
    
    
    
    
# def dict_of_numbers():
#     s = {
#         0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
#         6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
#         11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
#         15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 
#         19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 
#         50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
#     }
#     return s

# def number_to_word(num, s):
#     if num in s:
#         return s[num]
#     else:
#         tens = num // 10 * 10
#         ones = num % 10
#         return s[tens] + "-" + s[ones]

# if __name__== "__main__":
#     s = dict_of_numbers()
#     print(number_to_word(2, s))
#     print(number_to_word(11, s))
#     print(number_to_word(45, s))
#     print(number_to_word(99, s))
#     print(number_to_word(0, s))



def dict_of_numbers():
    s = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 
        50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }
    for i in range(21, 100):
        if i not in s:
            tens = i // 10 * 10
            ones = i % 10
            s[i] = s[tens] + "-" + s[ones]
    return s

if __name__== "__main__":
    s = dict_of_numbers()
    print(s[2])
    print(s[11])
    print(s[45])
    print(s[99])
    print(s[0])
