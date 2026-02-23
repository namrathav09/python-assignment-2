year=int(input("Enter the year:"))
    
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Year:",year,"\nWhether leap year or no:Is a leap year.")
    if year%400==0:
       print("Reason:It is divisible by 400")
    else:
        print("Reason:It is divisible by 4 and not divisible by 100")
else:
    print("Year:",year,"\nWhether leap year or no:Not a leap year.")
    if year%4!=0:
        print("Reason:It is not divisible by 4")
    else:
        print("Reason:It is divisible by 100 but not divisible by 400") 
    
