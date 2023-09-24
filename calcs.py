def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def times(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Number shouldn't be divided by 0"
    return num1 / num2

try:
    print("A Simple Calculator")
    print("=======================")
    num1 = float(input("Input the first variable: "))
    num2 = float(input("Input the second variable: "))
    print("=======================")
    print("Operasi")
    print("1. Add")
    print("2. Subtract")
    print("3. Times")
    print("4. Divide")
    operation = input(str("Choose operation: "))

    if(operation == "1"):
        typeOfOperation = "Addition"
        result = add(num1, num2)
    elif(operation == "2"):
        typeOfOperation = "Substraction"
        result = substract(num1, num2)
    elif(operation == "3"):
        typeOfOperation = "Times"
        result = times(num1, num2)
    elif(operation == "4"):
        typeOfOperation = "Divide"
        result = divide(num1, num2)
    else:
        result = "Operation not valid"
    
    print(typeOfOperation,"result = ",result)

except ValueError:
    print("The number wasn't a valid number, please input a valid number")

