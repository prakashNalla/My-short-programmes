#!/usr/bin/env python3.10
import random

"""
a beta-level stone/paper/scissor game
has to implemented
"""

INCREASE_SCORE, DECREASE_SCORE = 1, 0  # increase/decrease score
OPTIONS = ["stone","paper","scissors"]  # all options as of now
PLAYER, CPU, DRAW, NUMBER_OPTIONS = 0, 0, 0, len(OPTIONS)  # scores & no. of options
DEFAULT_RUN_GAME, DEFAULT_NUMBER_ROUNDS = 'n', 3  # fallback variables
# messages to be displayed
WON_MESSAGE, LOST_MESSAGE, DRAW_MESSAGE = "You Won!", "You Lost", "Drawn"  # messages

NUMBER_ROUNDS = input("Number of rounds you want -> ")  # input number of rounds
if not NUMBER_ROUNDS.isdecimal():  # check if given no. is a int
    NUMBER_ROUNDS = DEFAULT_NUMBER_ROUND
else:
    NUMBER_ROUNDS = int(NUMBER_ROUNDS)

if not isinstance(
        (RUN_GAME := input("Want to play? (y/n) -> ")[0].lower()),
        str
    ) or RUN_GAME != 'y': # check if input credentials are correct
    RUN_GAME = DEFAULT_RUN_GAME


def welcome():
    """ Returns Welcome Message """
    return (
            "Welcome to Stone/Paper/Scissors!\n"
            "1 -> Stone\n"
            "2 -> Paper\n"
            "3 -> Scissor"
        )

def game_logic(
    player_score=PLAYER,
    cpu_score=CPU,
    draw_score=DRAW):
    """ Run the Stone/Paper/Scissors game """
    if not isinstance(
        (player := int(input("what's your bet? -> "))),
        int
    ) or player not in range(1, NUMBER_OPTIONS+1):  # get and check input option
        return
    # random option(chosen by the random module)
    cpu = random.randrange(1, NUMBER_OPTIONS)
    if player == cpu:  # if draw
        draw_score += INCREASE_SCORE
        print(DRAW_MESSAGE)
    elif player - cpu in range(1, NUMBER_OPTIONS+1):  # if player won
        print(WON_MESSAGE)
        player_score += INCREASE_SCORE
        cpu_score -= DECREASE_SCORE
    elif player - cpu in range(-1, -1*(NUMBER_OPTIONS+1), -1): # if player lost
        print(LOST_MESSAGE)
        cpu_score+= INCREASE_SCORE
        player_score-= DECREASE_SCORE
    else: # sure nothing would go wrong, but still, idk mcbc
        print(player, cpu)
    # program ran successfully without any exceptions
    return player_score, cpu_score, draw_score


def final_scores( player_score, cpu_score, draw_score):
    """ Prints Final ScoreBoard"""
    baseline_scoreboard = (
        f"Player Score -> {player_score}\n"
        f"CPU Score -> {cpu_score}\n"
        f"Draw Score -> {draw_score}"
    )  # base message for all other detailed ones
    if player_score > cpu_score: # player won
        return (
            f"{WON_MESSAGE}\n"
            f"{baseline_scoreboard}"
        )
    if cpu_score > player_score: # player lost
        return (
            f"{LOST_MESSAGE}\n"
            f"{baseline_scoreboard}"
        )
    return (  # Draw
        f"{DRAW_MESSAGE}\n"
        f"{baseline_scoreboard}"
    )


def main():
    """ Main Function """
    global PLAYER, CPU, DRAW
    quit_game = False
    # start game
    print(welcome())
    while RUN_GAME == 'y':
        for _ in range(NUMBER_ROUNDS): # run game till given output
            scores = game_logic() # stat game
            if scores is None:
                break
            PLAYER, CPU, DRAW = map(
                    lambda score: sum(score),
                    zip((PLAYER, CPU, DRAW), scores) 
                ) # set and update scores
        if not scores is None:  # print final scorecard
            # print(PLAYER, CPU, DRAW)
            print(f"\n{final_scores(PLAYER, CPU, DRAW)}")  # final scores
        break  # break the loop once done
    


if __name__ == '__main__': # run
    main()
