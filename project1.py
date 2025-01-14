import random

def roll():
    min_val= 1
    max_val= 6
    roll= random.randint(min_val, max_val)
    return roll

while True:
    players= input("Enter the number of players (2-4): ")
    if players.isdigit():
        players= int(players)
        if 2<=players<=4:
            break
        else:
            print("Number of players must be between 2-4")
    else:
        print("Invalid input, try again")

max_score= input("Enter the maximum possible score: ")
player_scores= [0 for k in range(players)]

while max(player_scores)<int(max_score):
    for i in range(players):
        track= 0
        print("Player ",i+1,"'s turn:")
        while True:
            sr= input("Would you like to roll (y)? ")
            if sr!="y" and sr!="Y":
                break
            value= roll()
            if value==1:
                print("You rolled a 1!\nTurn over!")
                track= 0
                break
            else:
                track+= value
                print("You rolled a ", value)
                if value>=int(max_score) or track>=int(max_score):
                    print("Player",i+1,"'s total score= ", track)
                    print("Player ", i+1," has won!")
                    exit()
        player_scores[i]+= track
        print("Player",i+1,"'s total score= ", player_scores[i])
        if player_scores[i]>=int(max_score):
            print("Player ", i+1," has won!")
            break