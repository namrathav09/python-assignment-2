n=int(input("Enter the number for table generation:"))

end=int(input("The number range till where the table prints:"))

for i in range(1,end+1):
    print(n,"x",i,"=",n*i)

#Bonus points
#full multiplication table (1-10 for all numbers 1-10) in grid format.
print("Multiplication table from 1-10")

for i in range(1,11):
    for j in range(1,11):
        print (f"{i*j:4}",end=" ") #here as the number from 1 to 100 is present there is a need for spaces in between n umber so i have given :4 space 
    print()


