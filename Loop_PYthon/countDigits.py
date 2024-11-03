number=int(input("Enter the number :"))
number=abs(number)
if (number==0):
    count=1
else:
    count=0
    
while number>0:
    number//=10
    count+=1
    

print(count)