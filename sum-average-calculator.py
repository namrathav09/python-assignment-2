count=int(input("Enter total number you want to print:"))

numbers=[]

for i in range(count):
    num=float(input(f"Enter number {i+1}:"))
    numbers.append(num)

add_numbers=sum(numbers)
average_of_numbers=add_numbers/count
maximum_number=max(numbers)
minimum_number=min(numbers)

print("--------------")
print("\nSum of all number:",add_numbers)
print("Average of all numbers:",average_of_numbers)
print("Maxinmum number:",maximum_number)
print("Minimum numbers:",minimum_number)
