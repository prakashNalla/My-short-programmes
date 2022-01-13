#!/usr/bin/env python3.10
import random

"""
a beta-level stone/paper/scissor game
has to implemented
"""

INCREASE_SCORE, DECREASE_SCORE = 1, 0  # increase/decrease score
CONFIRM_RUN = 'y'
OPTIONS = ["stone","paper","scissors"]  # all options as of now
PLAYER, CPU, DRAW, NUMBER_OPTIONS = 0, 0, 0, len(OPTIONS)  # scores & no. of options
DEFAULT_RUN_GAME, DEFAULT_NUMBER_ROUNDS = 'n', 3  # fallback variables
# messages to be displayed
WON_MESSAGE, LOST_MESSAGE, DRAW_MESSAGE = "You Won!", "You Lost", "Drawn"  # messages


def welcome():
    """ Returns Welcome Message """
    return (
            "Welcome to Stone/Paper/Scissors!\n"
            "1 -> Stone\n"
            "2 -> Paper\n"
            "3 -> Scissor"
        )


def get_run_game_confirmation():
    """ Returns response from player """
    # check if input credentials are correct
    if not (run_game := input("Want to play? (y/n) -> ").lower()) == CONFIRM_RUN:
        return DEFAULT_RUN_GAME
    return run_game


def get_number_rounds():
    """ Return number of rounds player inputs """
    number_rounds = input("Number of rounds you want(3) -> ")  # input number of rounds
    if not number_rounds.isdecimal():  # check if given no. is a int
        return DEFAULT_NUMBER_ROUNDS
    return int(number_rounds)


def game_logic(
    player_score=PLAYER,
    cpu_score=CPU,
    draw_score=DRAW):
    """ Run the Stone/Paper/Scissors game """
    if (
        player := int(input("what's your bet? -> "))
        ) not in range(1, NUMBER_OPTIONS+1):  # get and check input option
        return
    # random option(chosen by the random module)
    cpu = random.randrange(1, NUMBER_OPTIONS+1)
    print(
        ("==>-==>-===-<==-<==\n"
        f"PLAYER: {OPTIONS[player-1].title()}\n"
        f"CPU:    {OPTIONS[cpu-1].title()}\n"
        "==>-==>-===-<==-<==")
        )
    if player == cpu:  # if draw
        draw_score += INCREASE_SCORE
        print(DRAW_MESSAGE)
    elif player - cpu in (1, -2):
        print(WON_MESSAGE)
        player_score += INCREASE_SCORE
        cpu_score -= DECREASE_SCORE
    elif player - cpu in (-1, 2): # if player lost
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
    print(welcome(), "\n")
    while get_run_game_confirmation() == CONFIRM_RUN:
        for _ in range(get_number_rounds()): # run game till given output
            scores = game_logic() # start game
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
