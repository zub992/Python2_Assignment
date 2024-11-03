import time
n=int(input("Enter the Number to Start the Countdown to Zero :"))
for i in range(n,-1,-1):
    print(i)
    time.sleep(1)

print("Countdown Finished")