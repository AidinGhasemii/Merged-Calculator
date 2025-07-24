def add(x, y): #function for sum
    return x + y

def subtract(x, y): #function for difference
    return x - y


def calculator(): # function for calculator
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")

    while True:
        choice = input("Enter choice (1/2): ")

        if choice in ['1', '2']: # getting numbers from user if operation true
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

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

