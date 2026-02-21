def pattern1(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def pattern2(height):
    for i in range(1, height + 1):
        for j in range(i):
            print(i, end="")
        print()


def pattern3(height):
    for i in range(height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


def pattern4(height):
   
    for i in range(1, height + 1):

        # spaces
        for space in range(height - i):
            print(" ", end="")

        # increasing numbers
        for j in range(1, i + 1):
            print(j, end="")

        # decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")

        print()


def main():
    print("Choose a Pattern:")
    print("1. Pattern 1")
    print("2. Pattern 2")
    print("3. Pattern 3")
    print("4. Pattern 4")

    choice = int(input("Enter your choice (1-4): "))
    height = int(input("Enter the height: "))
    print("The option you chose is:",choice)
    print("The pattern :")
    
    
    if choice == 1:
        pattern1(height)
    elif choice == 2:
        pattern2(height)
    elif choice == 3:
        pattern3(height)
    elif choice == 4:
        pattern4(height)
    else:
        print("The option you chose is invalid")


main()
