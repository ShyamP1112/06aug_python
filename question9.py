# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))

if num1==num2 or num2==num3 or num1==num3:
    print("sum will be zero")
else:
    sum=num1+num2+num3
    print(sum)
