import random
def main():
    print("Welcome to Rock, Paper, Scissors Game!!!")
    RPS = ["rock", "paper", "scissors"]
    play_again = "y"

    while play_again == "y":
        playerChoice = input("Lets play. Choose one: rock, paper, or scissors.\n")
        computerChoice = random.choice(RPS)

        print(f"Computer selected: {computerChoice}")
        print(f"Player selected: {playerChoice}")

        if(playerChoice == computerChoice):
            print("You tied @_@")
        elif(playerChoice == "rock" and computerChoice == "paper"):
            print("Paper devours rock. You lost >_<")
        elif(playerChoice == "rock" and computerChoice == "scissors"):
            print("Rock crushes siccors. YOU WON! :)")
        elif(playerChoice == "paper" and computerChoice == "rock"):
            print("Paper devours rock. YOU WON! :)")
        elif(playerChoice == "paper" and computerChoice == "scissors"):
            print("Scissors cuts through paper. You lost >_<")
        elif(playerChoice == "scissors" and computerChoice == "rock"):
            print("Rock crushes scissors. You lost >_<")
        elif(playerChoice == "scissors" and computerChoice == "paper"):
            print("Scissors cuts through paper. YOU WON! :)")
        else:
            print("Something isn't right. Maybe try again")    
        play_again = input("Play again? Enter 'y' for yes or 'n' for no.")
    print("Game Over")
main()
   