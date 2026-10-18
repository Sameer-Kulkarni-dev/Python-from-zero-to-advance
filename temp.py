"""
temp is 50-25 = hot
temp is 18-24=cold
temp is 1-17=frezzing
"""

temp=int(input("enter your city temperature ") )

if temp<=50 and temp>=25:
    print("hot")
elif temp<=24 and temp>=18:
    print("cold")
elif temp<17:
    print("frezzing cold")

print(temp)