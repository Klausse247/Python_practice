def calculate(value, value_2, operator):
    if operator == '+':
        return value + value_2
    elif operator == '-':
        return value - value_2
    elif operator == '*':
        return value * value_2
    elif operator == '/':
        return value / value_2 if value_2 != 0 else None

while True:
    try:
        value = float(input("Give me the first value: "))
        value_2 = float(input("Give me the second value: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    operator = input("Enter operation (+, -, *, /): ")
    if operator not in ['+', '-', '*', '/']:
        print("Invalid operator! Please enter one of (+, -, *, /).")
        continue

    result = calculate(value, value_2, operator)

    if result is None:
        print("You cannot divide by zero!")
    else:
        print("Result:", result)

    if input("Perform another operation? (yes/no): ").lower() != 'yes':
        print("Thank you for using the calculator!")
        break





# while True:                                                                         #Loop starts and calculator continues to run
#     try:
#         value = float(input("Give me the first value: "))                           #asking for first and second value while doing a check if its a number
#         value_2 = float(input("Give me the second value: "))      
#     except ValueError:
#         print ("Invalid input! please enter a valid number")
#         continue                                                                 #Loop starts and calculator continues to run
    
#     operator = input("Enter what operation you want to use (+, -, *, /): ")     #asking which operation the user wants to use

#             # if and elif operators to determine what the user wants to do
#     if operator == '+':
#         result = value + value_2
#     elif operator == '-':
#         result = value - value_2
#     elif operator == '*':
#         result = value * value_2
#     elif operator == '/': 
#         if value_2 == 0:
#             print ("you cannot divide by zero!")
#             result = None
#         else:
#             result = value / value_2

#     else:
#         print("Invalid operator! Please enter one of (+, -, *, /).")
#         continue  # Restarts the loop if the operator is invalid
        
#     if result is not None:
#             print (result)

#     cont = input("Do you want to perform another operation? (yes/no): ").lower()
#     if cont != 'yes':
#         print ("Thank you for using the Calculator ")
#         break  

'''
print ("first number is:" , value)
print ("second number is: " , value_2)
print ("addition is :", result)
'''


#result = value + value_2
'''value = float(input("what numbers would you like to add: "))
print("Your number is:" , value)'''