print("Welcome to Python Calculator :")
num1=int(input("Enter 1st Number: "))
num2=int(input("Enter 2nd Number: "))
print("+","-","*","/")
operation=str(input("choose an operation: "))
if operation=="+":
    print(num1+num2)
elif operation=="-":
    print(num1-num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    print(num1/num2)
else:
    print("invalid operation please choose valid operation")
