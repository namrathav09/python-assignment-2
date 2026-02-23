your_input=input("Enter a number or word:")

print("Original:",your_input)

#reversing the input
reverse_input=your_input[::-1]
print("Reversed:",reverse_input)

#tomake case insensitive we used lower()
if your_input.lower()==reverse_input.lower():
    print("Result:PALINDROME")
else:
    print("Result:Not a PALINDROME")
