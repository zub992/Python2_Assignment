year=int(input("Enter the year : "))
if(year%400==0 and year%100==0):
    print(year," : This year is leap year")
elif(year%4==0 and year%100!=0):
    print(year,": This is leap year")
else:
    print(year,": This is not leap year")