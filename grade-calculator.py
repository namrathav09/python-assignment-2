#To enter every subject marks
science_marks=int(input("Enter your SCIENCE marks:"))
maths_marks=int(input("Enter your MATHEMATICS marks:"))
social_marks=int(input("Enter your SOCIAL marks:"))
kannada_marks=int(input("Enter your KANNADA marks:"))
hindi_marks=int(input("Enter yor HINDI marks:"))

total_marks=science_marks+maths_marks+social_marks+kannada_marks+hindi_marks
print("Your total marks is:",total_marks)

percentage=(total_marks/500)*100
print("Your percentage is:",percentage)

if percentage>=90:
    print("A+ (Outstanding)")
elif percentage>=80:
    print("B (Excellent)")
elif percentage>=70:
    print("C (Good)")
elif percentage>=60:
    print("D (Pass)")
else:
    print("F (Fail)")

if science_marks>=40 and maths_marks>=40 and social_marks>=40 and kannada_marks>=40 and hindi_marks>=40:
    print("Grade:Pass")
else:
    print("Grade:Fail")

