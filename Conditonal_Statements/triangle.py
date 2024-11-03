a=float(input("Enter the  First side "))
b=float(input("Enter the Second side"))
c=float(input("Enter the Third side"))
if(a+b>c and a+c>b and b+c>a):
    print("This is the valid triangle")
else:
    print("This is not valid triangle")