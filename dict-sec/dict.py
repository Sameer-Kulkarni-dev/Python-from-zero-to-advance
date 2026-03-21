marks={}
x=int(input("enter the marks of math: "))
marks.update({"math": x})

y=int(input("enter phy " ))
marks.update({"phy":x})

z=int(input("enter the chem "))
marks.update({"chem":z})

print(marks)
print(len(marks))