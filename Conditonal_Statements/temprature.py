temprature=float(input("Enter the temprature in Celsius :"))
if(temprature<0):
    print("It is Freezing Temprature")
elif(temprature>0 and temprature<=25):
    print("It is Moderate Temprature")
else:
    print("It is Hot Temprature")