def get_choices():
    player_choice= input("Enter your choce (Rock , Paper , Scisessor) \n")
    computer_choice= "paper"
    choices={"player" :player_choice ,"computer":computer_choice }
    return choices

choices=get_choices()
print(choices)
