number=int(input("Enter the number : "))
factorial=1
for i in range (number,0,-1):
    factorial*=i
    
    
print("factorial of ",number,"is",factorial)