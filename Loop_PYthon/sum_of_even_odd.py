n = int(input("Enter the number: "))
sum_even = 0
sum_odd = 0

for i in range(1, n + 1):  
    if i % 2 == 0:
        sum_even += i  
    else:
        sum_odd += i  

print("The sum of even is", sum_even, "The sum of odd is", sum_odd)

