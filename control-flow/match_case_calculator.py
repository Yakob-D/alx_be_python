num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /) ")

match operation:
    case '+':
        result = num1 + num2
        print(result)
    case '-':
        result = num1 - num2
        print(result)
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 - num2
            print(result)
    case '*':
        result = num1 * num2
        print(result)
    case _ :
        print("Invalid operation.")