total_bill=float(input("Enter your total bill:"))
total_people=float(input("Enter total number of people:"))
tax_percentage=int(input("Enter tax percentage:"))
tip_percentage=float(input("Enter tip percentage:"))

print("---Bill BREAKDOWN---")

print("Subtotal:₹",total_bill)

tax_cost=(total_bill/100)*10
print("Tax",tax_percentage,"%:₹",tax_cost)

bill_after_tax=total_bill+tax_cost
print("Bill after tax:₹",bill_after_tax)

tip_cost=(bill_after_tax/100)*15
print("Tip",tip_percentage,"%:₹",tip_cost)

total_cost=total_bill+tax_cost+tip_cost
print("Total:₹",total_cost)

cost_per_person=total_cost/total_people
print("Per person:₹",cost_per_person)