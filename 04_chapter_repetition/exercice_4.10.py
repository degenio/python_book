flag = True

while flag:
    print("================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Quit")
    print("================")
    
    option = int(input("Enter a menu option 1-4: "))

    if option == 4:
        print("Thank you for using our application.")
        flag = False
    elif 1 <= option <= 3:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        
        if option == 1:
            result = a + b
        elif option == 2:
            result = a - b
        else:
            result = a * b
        
        print("Result of the operation: {}".format(result))
    else:
        print("Invalid menu option")
