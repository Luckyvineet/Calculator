print(" MINI CALCULATOR")
num1=float(input("enter your first number: "))
num2=float(input("enter your second number: "))
print("press 1 for addition","press 2 for subtraction","press 3 for multiplication","press 4 for division",sep="\n")
choice=int(input("enter your choice: "))
if choice == 1:
    print("the addition of given numbers is ", num1+num2)
elif choice == 2:
    print("the subtraction of given numbers is ", num1-num2)
elif choice == 3:
    print("the multiplication of given numbers is ", num1*num2)
elif choice == 4:
    print("the division of given numbers is ", num1/num2)
else:
    print("Invalid Input")