import random

run = "y"
round = 1 
player_points = 0
CPU_points = 0
draw = 0 
l = ["Stone","Paper","scissors"]

while run == "y":
    while(round <= 10) :    
        try :
            print(f"Round = {round}")
            cpu_choose = random.choice(l)
            player_choose = int(input("1 for stone\n2 For Paper\n3 For Scissors\n"))
            player_choose2 = l[player_choose - 1 ]
            if player_choose2 == cpu_choose :
                print("Match draw\n")
                draw += 1
            elif player_choose == 1 and cpu_choose ==l[3 -1]:
                print(f"You Won")
                player_points += 1 
            elif player_choose == 1 and cpu_choose ==l[2 - 1]:
                print(f"You lost")
                CPU_points += 1 
            elif player_choose == 2 and cpu_choose ==l[3 - 1]:
                print(f"You lost")
                CPU_points += 1 
            elif player_choose == 2 and cpu_choose ==l[1 - 1]:
                print(f"You Won")
                player_points += 1 
            elif player_choose == 3 and cpu_choose ==l[1 - 1]:
                print(f"You Lost")
                CPU_points += 1 
            elif player_choose == 3 and cpu_choose ==l[2 - 1]:
                print(f"You Won")
                player_points += 1 
            else :
                print("Wrong input try Again")
        except Exception as p:
            print(p)
        round += 1
  
    if player_points > CPU_points :
        print(f"You won\nYour score = {player_points}\nCPU Score = {CPU_points}\nDraw = {draw}")
    elif player_points < CPU_points :
        print(f"CPU won\nYour score = {player_points}\nCPU Score = {CPU_points}\nDraw = {draw}")
    elif player_points == CPU_points :
        print(f"Draw\nYour score = {player_points}\nCPU Score = {CPU_points}\nDraw = {draw}")
    run = input("press 'y' to play again and 'n' to exit")
print("\nThx for playing\n")