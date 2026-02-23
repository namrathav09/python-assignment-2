while True:
    print("Temperature converter!")

    print("\nChooose any of the option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. exit")

    option=int(input("\nEnter your choice:"))

    if option==1:
        c=float(input("Celsius:"))
        f=(c * 9/5) + 32 
        print("Temperature in Fahrenheit is:",f)

    elif option==2:
        f=float(input("Fahrenheit:"))
        c=(f - 32)* 5/9 
        print("Temperature in Celsius is:",c)

    elif option==3:
        c=float(input("Celsius:"))
        k=c + 273.15 
        print("Temperature in Kelvin is:",k)

    elif option==4:
        k=float(input("Kelvin:"))
        c=k - 273.15 
        print("Temperature in Celsius is:",c)

    elif option==5:
        f=float(input("Fahrenheit:"))
        k=(f - 32) * 5/9 + 273.15  
        print("Temperature in Kelvin is:",k)

    elif option==6:
        k=float(input("Kelvin:"))
        f=(k - 273.15)* 9/5 + 32  
        print("Temperature in Fahrenheit is:",f)

    elif option==7:
        print("Your program is exited")
        break

    else:
        print("Option invalid")





