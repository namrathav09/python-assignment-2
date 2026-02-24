def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    answer = 1
    for i in range(1, n + 1):
        answer = answer * i

    return answer

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def fibonacci(n):
    if n <= 0:
        return "Invalid input"

    if n == 1:
        return 0

    if n == 2:
        return 1

    first = 0
    second = 1

    for i in range(3, n + 1):
        next_number = first + second
        first = second
        second = next_number

    return second


def sum_of_digits(n):
    total = 0
    number = abs(n)

    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10

    return total

def reverse_number(n):
    reversed_number = 0
    number = abs(n)

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    if n < 0:
        return -reversed_number
    else:
        return reversed_number


def is_armstrong(n):
    number = abs(n)
    total = 0
    digits = len(str(number))
    temp = number

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10

    if total == number:
        return True
    else:
        return False

def gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0

    gcd_value = gcd(a, b)
    lcm_value = abs(a * b) // gcd_value

    return lcm_value

def is_perfect_number(n):
    if n <= 1:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i

    if total == n:
        return True
    else:
        return False

def math_menu():
    while True:
        print("\n----------- MATH MENU -----------")
        print("1. Factorial")
        print("2. Check Prime")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == "10":
            print("Exited number system!")
            break

        elif choice == "1":
            n = int(input("Enter a number: "))
            print("Factorial is:", factorial(n))

        elif choice == "2":
            n = int(input("Enter a number: "))
            print("Is Prime:", is_prime(n))

        elif choice == "3":
            n = int(input("Enter position: "))
            print("Fibonacci number is:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter a number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter a number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter a number: "))
            print("Is Armstrong number:", is_armstrong(n))

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD is:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM is:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter a number: "))
            print("Is Perfect number:", is_perfect_number(n))

        else:
            print("Invalid choice. Please try again.")


math_menu()