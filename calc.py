def multiply(x, y):# function for multiply
    return x * y

def divide(x, y):# function for divide
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator(): # function for calculator
    print("Simple Calculator")
    print("Select operation:")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (3/4): ")

        if choice in ['3', '4']: # getting numbers from user if operation true
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            # Ask if user wants another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
############################################as

