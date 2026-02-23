age=int(input("Enter your age:"))
day=input("Enter day of the week:").lower()
number_of_tickets=int(input("number of tickets:"))

if age<=3:
    ticket_price=0
    print("Free ticket")
elif 3<= age <=12:
    ticket_price=150
    print("Child")
elif 13<= age <=59:
    ticket_price=300 
    print("Adult")
elif age >=60 : 
    ticket_price=200
    print("Senior")
    
total_ticket_price=number_of_tickets*ticket_price

if day in ("friday","saturday","sunday"):
    discount=total_ticket_price*0.20
    print("Discount applied!")
else:
    discount=0
    print("Discount not applicable!")

final_price=total_ticket_price-discount
print("You have to pay:",final_price)

    

