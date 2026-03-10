num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
num3=int(input("enter the number 3:"))
if(num1>num2 and num1>num3):
    print("the largest number is ",num1)
elif(num2>=num3):
    print("the largest number is ",num2)
else:    print("the largest number is ",num3)

# logic behind this is if num1 is greater than num2 and num3 then num1 is the largest number, otherwise if num2 is greater than or equal to num3 then num2 is the largest number, otherwise num3 is the largest number.