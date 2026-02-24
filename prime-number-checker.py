
def find_prime_numbers(start, end):

    print("Prime numbers between", start, "and", end, "are:")

    for number in range(start, end + 1):

        if number <= 1:
            continue

        is_prime_number = True

        for i in range(2, number):
            if number % i == 0:
                is_prime_number = False
                break

        if is_prime_number:
            print(number, end=" ")


start_range = int(input("Enter the starting number: "))
end_range = int(input("Enter the ending number: "))

find_prime_numbers(start_range, end_range)