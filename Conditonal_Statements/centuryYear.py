year=int(input("Enter the Year :"))
if(year%100==0 and year>0):
    print(f"{year} is the century year")
else:
    print(year,"This is not century year ")
