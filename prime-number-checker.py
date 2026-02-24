def check_prime(number):

    if number <= 1:
        return False

    if number == 2:
        return True

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if check_prime(num):
    print(num, "is a Prime number.")
else:
    print(num, "is not a Prime number.")