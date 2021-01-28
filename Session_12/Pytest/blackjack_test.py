import random

#Random Blackjack Generator
n = random.randint(1, 11)
x = random.randint(1, 11)

#Dealer
dealer_total = 0

#Start Game
player_name = input("Whats your name? ")
#Players Start with 50 Chips Default
player = {
    "chips-count": 50, 
    }
chips = player["chips-count"]
player_total = 0

#Actions - Where the players are able to play a hand or leave the table
choice = ["Yes", "No"]
actions = ["Hit", "Fold", "Out", "Bet", "Chip Count "]

while chips > 0:

    for actions in actions:
        print(actions)

    action = input("What would you like to do? ")

    #Playing the game
    if action == "Hit":
        player_total = player_total + n
        n = random.randint(1, 11)
        player_total = str(player_total)
        print(player_name  +  player_total)
        player_total = int(player_total)
        if player_total > 21:
            print("You lose! ")
        else:
            if player_total == 21:
                print("You WIN! ")

    #Folding to see if you win... dealer will draw cards...
    if action == "Fold":
        dealer_total = dealer_total + x
        player_total = str(player_total)
        print(player_name  +  player_total)
        player_total = int(player_total)
        print(x)
        x = random.randint(1, 11)
        print(x)
        x = random.randint(1, 11)
        print(x)
        x = random.randint(1, 11)
        dealer_total = str(dealer_total)
        print("Dealer "  +  dealer_total)
        dealer_total = int(dealer_total)
        if dealer_total < player_total:
            print("You WIN! ")
        elif dealer_total == 21:
                print("You Lose! ")
        else:
            if dealer_total > player_total:
                print("You Lose! ")



    #The option to leave the game
    if action == "Out":
        choice = input("would you like to leave the table? ")
        if choice == "Yes":
            chips -=50
        if choice == "No":
            print("Lets get back to it then... ")