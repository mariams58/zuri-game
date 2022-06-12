# creating a list of all viable options for the game.
import random

opt_list = ["R", "P","S","r","s","p"]
print("Welcome! \n To the classic game  of Rock-Paper-Scissors ")
name = input("Please enter player name: ")
user_score= 0
com_score = 0
is_playing = True
rounds = 0

while is_playing:
    user_opt= str(input("Please choose your option: 'R' 'P' or 'S'"))
    for i in opt_list:
        if user_opt not in opt_list:
            print("Invalid Option!")
            user_opt= str(input("Choose a valid option: 'R' 'P' or 'S' "))        

    print("CPU is choosing an option...")
    
    com_opt = random.choice(opt_list)
    
    print('CPU(',com_opt, ") VS", name,"(",user_opt,")")
    if user_opt == com_opt:
        rounds += 1
        print("It is a tie. Keep trying!")
        continue
    elif user_opt =="R":
        if com_opt=="S":
            print("Rock beats scissors")
            print(name, "wins")
        else:
            print("Paper beats rock")
            print("CPU wins")
            com_score += 1
        rounds +=1
        
    
    elif user_opt=="S": 
        if com_opt=="P":
            print("Scissors beats paper")
            print(name, "wins")
            user_score += 1
        else:
            print("Rock beats scissors ")
            print("CPU wins")
            com_score +=1
        rounds +=1

    elif user_opt == "P": 
        if com_opt=="R":
            print("Paper beats rock")
            print(name, "wins")
            user_score += 1
        else:
            print("Scissors beats paper")
            print("CPU wins")
            com_score += 1
        rounds += 1
    
    elif rounds > 2 and com_score!=user_score:
        break
    is_playing = False
    if com_score > user_score:
            #is_playing = False
        print("CPU wins the game")
    else:
            #is_playing = False
        
        print(name, "wins the game.")
        
print("Thanks for playing my game! \n GOODBYE")
