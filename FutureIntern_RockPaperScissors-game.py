import random

while True:
    player_input = input("Enter your choice = (rock, paper, scissor)")
    item_list =["rock", "paper", "scissor"]
    computer_input =random.choice(item_list)

    print(f"You chose {player_input}, computer chose {computer_input}")

    if player_input == computer_input:
            print(f"Its a Draw as both selected {player_input}")
    elif player_input == "rock":
        if computer_input == "scissor":
            print("Player wins, Rock will break the scissor")
        else:
            print("Player lose, Paper will cover rock")
        
    elif player_input == "paper":
        if computer_input == "rock":
            print("Player wins, Paper will cover rock")
        else:
            print("Player lose, Scissor will cut  the paper")
        
    elif player_input == "scissor":
        if computer_input == "paper":
            print("Player wins, Scissor  will cut the paper")
        else:
            print("Player lose, Rock will cut the scissor")

    play_again = input("Do you want to play again?(y/n): ")
    if play_again.lower() !=  "y":
        break

print("Game Over")