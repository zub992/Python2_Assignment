number=int(input("Enter the Integer "))
if(number%2==0 and number%3==0):
    print(number,"is Divisible by both 2 and 3")
elif(number%2==0):
    print(number," is only divisible by 2")
elif(number%3==0):
    print(number,"is only divisble by 3")
else:
    print("invalid input")
