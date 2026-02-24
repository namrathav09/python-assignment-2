# Program to calculate factorial using loop

number = int(input("Enter a number to find its factorial: "))

# Handle negative numbers
if number < 0:
    print("Factorial is not defined for negative numbers.")

# Handle 0 separately
elif number == 0:
    print("Factorial of 0 is 1.")
    print("Because 0! = 1 by definition.")

else:
    factorial = 1
    print("Calculations:")

    for i in range(number, 0, -1):
        print(i, end="")

        if i != 1:
            print(" × ", end="")
        else:
            print(" = ", end="")

        factorial = factorial * i

    print(f"Factorial of {number} is:",factorial)