num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operation=input("Choose the operation (+, -, *, /): ")
if operation=='+':
    print(num1+num2)
elif operation=='-':
    print(num1-num2)
elif operation=='*':
    print(num1*num2)
elif operation=='/' and num2 != 0:
    print(num1/num2)
else:
    print("Cannot divide by zero.")
