# marks={}
# x=int(input("enter the marks of math: "))
# marks.update({"math": x})

# y=int(input("enter phy " ))
# marks.update({"phy":x})

# z=int(input("enter the chem "))
# marks.update({"chem":z})

# print(marks)
# print(len(marks))



#Dict are the thing in python which is represented as key value pairs

def get_choices():
    player_choice= input("Enter your choce (Rock , Paper , Scisessor) \n")
    computer_choice= "paper"
    choices={"player" :player_choice ,"computer":computer_choice }
    return choices

choices=get_choices()
print(choices)

