print("choose operation")
print("1.ADD")
print("2.SUBSTRUCT")
print("3.DIVISION")
print("4.MULTIPLY")

op = input()

if op == "1":
    num1 = input("Enter first number ")
    num2= input("Enter second number ")
    print("The sum is: " + str(int (num1) + int (num2)))
    
elif op == "2":
    num1 = input("Enter first number ")
    num2= input("Enter second number ")
    print("The sum is:  " + str(int (num1) - int (num2)) )  
    
elif op =="3":
    num1 = input("Enter first number ")
    num2= input("Enter second number ")
    print("The sum is: " + str( int (num1) / int (num2)))
    
elif op =="4":
    num1 = input("Enter first number ")
    num2= input("Enter second number ")
    print("The sum is: " + str(int (num1) * int  (num2)))
    
else:
    print("invalid")
