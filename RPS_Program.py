#super detailed rps game!
#1) Multiplayer, Single player, Spectate

import random
choices = ['r','p','s']

#gamemode function
def gamemode(gamemode_choice):
    if gamemode_choice == "Multi":
        multiplayer_gamemode() #call multiplayer function
    if gamemode_choice == "Single":
        game_single_player()
    if gamemode_choice == "Spec": 
        spectator()

def game_single_player():
    #while ask_to_continue == "y" and player in choices: #This is not good, i'd need to create dummmy variable. instead i can do while True:
    computer_score = 0
    player_score = 0
    while True:
        computer = random.choice(choices)
        player = validate(input("r,p,s: "),['r','p','s'])
        """
        or you can do..
        player = input("r,p,s: ")
        player = validate(player,['r','p','s'])
        """
        if validate(player,['r','p','s']):                      #player not in choices
            print("computer chose: ",computer)
            #player = input("r,p,s: ")
        if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
            print("player has won the match.")
            player_score += 1
        elif player == computer:
            print("the match was a draw.")
        #elif not((player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p')): #or should i just do else: print("computer won")
        else:
            print("The computer has won the match.")
            computer_score += 1

        ask_to_continue = input("(y/n) to continue: ") #add validation later to this
        if validate(ask_to_continue(input),['y','n']) != "y": #the reason we do != "y" is so that if thats true we break and thats it. If its false, it'll simply not trigger the conditon and continue. Otherwise we need to put continue then break.
            break
    print("scores:\nPlayer:"+str(player_score)+"\nComputer:"+str(computer_score))

def spectator():
    computer_one_s = 0
    computer_two_s = 0
    while True:
        computer_one = random.choice(choices)
        computer_two = random.choice(choices)
        print(f"bot attacks:\nComputer_one={computer_one}\nComputer_two={computer_two}")
        if computer_one == computer_two: 
                print("The game was a tie!")
                #choices = ['rock','paper','scissors']
        elif (computer_one == choices[0] and computer_two == choices[2]) or (computer_one == choices[1] and computer_two == choices[0]) or (computer_one == choices[2] and computer_two == choices[1]):
            print("computer_one has won!")
            computer_one_s += 1 
        else: 
            print("computer_two has won!")
            computer_two_s += 1
        
        ask_to_continue = input("(y/n) to continue: ")
        if validate(ask_to_continue) != "y": #the reason we do != "y" is so that if thats true we break and thats it. If its false, it'll simply not trigger the conditon and continue. Otherwise we need to put continue then break.
            break
    print(f"score:\nComputer_one:\t{computer_one_s}\nComputer_two\t{computer_two_s}")

def multiplayer_gamemode():
    """
    This function is for multiplayer rps, it takes the users inputs and determines who won. 
    It also validates. It asks the user if they want to continue, then the responce is stored and validated with the if statement if validate(compare,lzst)
    This calls the function and we pass the argument of the users responce and we determine if its valid (within the valid choices) then it checks the return value
    if the return is not "y" that means its n because that sthe only other valid choice, so then it breaks."""
    name1 = input("player 1's name: ").title()
    name2 = input("player 2's name: ").title()
    user_one_s = 0
    user_two_s = 0
    print("Your choices are: r,p,s ")
    while True:
        user_one = validate(input(f"{name1}'s move: r,p,s: "),['r','p','s']).lower() #2 birds 1 stone. validate, there inputs.
        user_two = validate(input(f"{name2}'s move: r,p,s: "),['r','p','s']).lower()
        if user_one == user_two: 
            print("The game was a tie!")
        elif (user_one == "r" and user_two == "s") or (user_one == "p" and user_two == "r") or (user_one == "s" and user_two == "p"):
            print(f"{name1} has won!") 
            user_one_s += 1
        else: 
            print(f"{name2} has won!")
            user_two_s += 1
        ask_to_continue = input("(y/n) to continue: ")
        if validate(ask_to_continue) != "y": #the reason we do != "y" is so that if thats true we break and thats it. If its false, it'll simply not trigger the conditon and continue. Otherwise we need to put continue then break.
            break
    print(f"Score:\n{name1}:\t{user_one_s}\n{name2}:\t{user_two_s}")   

def validate(compare,lzt=['y','n']):
    while compare not in lzt: #this gets valid responce if its not already valid.
        compare = input("enter somthing valid: ") #new input 
    return compare

"""
def rps_checker(p1_name, p1_choice, p2_name, p2_choice):
    #score = 0
    if p1_choice == p2_choice:
        print("draw!")
        return (1,0)
    elif (p1_choice == "r" and p2_choice == "s") or (p1_choice == "p" and p2_choice == "r") or (p1_choice == "s" and p2_choice == "p"):
            print(f"{p1_name} has won!")
            return (0,0) 
    else:   
        print(f"{p2_name} has won!")
        return (0,1)


notes 11:57pm,june 27, 2022
- Add who wins
- Make more functions to simplify this
"""
gamemode_choice = input("Single,Multi,Spec: ") #arrange this in order at bottom
gamemode(validate(gamemode_choice, ["Single", "Multi", "Spec"]))

