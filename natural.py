num1 = int(input(""))
hold = num1
sum = 0

if num1 <= 0: 
   print("invalid") 
else: 
   while num1 > 0:
        sum = sum + num1
        num1 = num1 - 1;
   print(sum)
