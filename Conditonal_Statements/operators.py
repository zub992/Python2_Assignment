num1=float(input("Enter the First Number : "))
num2=float(input("Enter the Second Number : "))
operator=input("Enter the Operator (+,-,/,*) : ")
if(operator=='+'):
    result=num1+num2
    print("The Answer is ",result)
elif(operator=='-'):
    result=num1-num2
    print("The answer is ",result)
elif(operator=='*'):
    result=num1*num2
    print("The Answer is ",result)
elif(operator=='/'):
    if num2!=0:
        result=num1/num2
        print("The answer is ",result)
    else:
        print("0 is not Allowed")
    