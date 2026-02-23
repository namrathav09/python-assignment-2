current_year=int(input("Enter current year:"))
birth_year=int(input("Enter your birth year:"))

age=current_year-birth_year
print("Your age:",age)

month_in_year=12
age_in_months=age*12
print("Your age in months:",age_in_months,"months")

days_in_year=365
age_in_days=days_in_year*age
print("Your age in days:",age_in_days,"days")

hours_in_days=24
age_in_hours=hours_in_days*age_in_days
print("Your age in hours:",age_in_hours,"hours")

minutes_in_an_hour=60
age_in_minutes=age_in_hours*minutes_in_an_hour
print("Your age in minutes:",age_in_minutes,"minutes")

years_until_age_100=100-age
print("Years until age 100:",years_until_age_100,"years")


