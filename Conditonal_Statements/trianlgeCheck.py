a=float(input("Enter the length of side a:"))
b=float(input("Enter the length of side b:"))
c=float(input("Enter the length of side c:" ))
if(a==b==c):
    print("The Triangle is Equilateral")
elif(a==b or b==c or c==a):
    print("The Triangle is isosceles")
else:
    print("The Triangle is scalene")