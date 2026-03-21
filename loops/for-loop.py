# nums=[100,200,300,400,500]

# for val in nums:
#     print(val)

# tup=(20,30,45,89,00,85)

# for val in tup:
#     if(val == 45):
#         continue
#     #val+=1
#     print(val)
#     val+=1



# str= " sameerkulkarni"

# for char in str:
#     if(char == "k"):
#         print(" k found ")
#         break
#     print(char)
# else :
#     print("end")

# list=[1,4,9,16,26,87,98,45,23]

# x=26
# idx=0

# for num in list:
#     if(num == x):
    
#      print("item found at idx ", idx)
#      break
    
#     idx+=1

# range function explanation sprcifies the range of the number for ex= if i give the input 5 it will take the range as 0-5
# means given number - 1 [ because of index starts fron the 0]

# for i in range(5):
#     print(i)

# print(range(5)) # o/p range (0,5) it is a object of range class
# print(list(range(5))) # o/p [0,1,2,3,4] it is a list of numbers from 0 to 4
# print(tuple(range(5))) # o/p (0,1,2,3,4) it is a tuple of numbers from 0 to 4


# for i in range (10,0,-2): # it will start from 2 and end at 10 with the step of 2 
#     # step can also be negative which means it will start from the given number and end at 0 with the step of 2
#     print(i)    


# n=int(input("enter the number : "))
# for i in range (1,11):
#     print(f"{n}  x  {i}  {n*i}")
    

n=5

fact=1

for i in range(1,n+1):
    fact *= i
    print("factorial number is ",fact)