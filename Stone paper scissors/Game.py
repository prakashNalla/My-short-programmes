#!/usr/bin/env python3.10
import random

INCREASE_SCORE, DECREASE_SCORE = 1, 0
OPTIONS = ["stone","paper","scissors"]
PLAYER, CPU, DRAW, NUMBER_OPTIONS = 0, 0, 0, len(OPTIONS)
DEFAULT_RUN_GAME, DEFAULT_NUMBER_ROUNDS = 'n', 3
# messages to be displayed
WON_MESSAGE, LOST_MESSAGE, DRAW_MESSAGE = "You Won!", "You Lost", "Drawn"

NUMBER_ROUNDS = input("Number of rounds you want -> ")
if not NUMBER_ROUNDS.isdecimal():
    NUMBER_ROUNDS = DEFAULT_NUMBER_ROUND
else:
    NUMBER_ROUNDS = int(NUMBER_ROUNDS)

if not isinstance(
        (RUN_GAME := input("Want to play? (y/n) -> ")[0].lower()),
        str
    ) or RUN_GAME != 'y':
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
    ) or player not in range(1, NUMBER_OPTIONS+1):
        return
    # random option(chosen by the random module)
    cpu = random.randrange(1, NUMBER_OPTIONS)
    if player == cpu:
        draw_score += INCREASE_SCORE
        print(DRAW_MESSAGE)
    elif player - cpu in range(1, NUMBER_OPTIONS+1):
        print(WON_MESSAGE)
        player_score += INCREASE_SCORE
        cpu_score -= DECREASE_SCORE
    elif player - cpu in range(-1, -1*(NUMBER_OPTIONS+1), -1):
        print(LOST_MESSAGE)
        cpu_score+= INCREASE_SCORE
        player_score-= DECREASE_SCORE
    else: # sure nothing would go wrong, but still
        print(player, cpu)
    # program ran successfully without any exceptions
    return player_score, cpu_score, draw_score


def final_scores( player_score, cpu_score, draw_score):
    """ Prints Final ScoreBoard"""
    baseline_scoreboard = (
        f"Player Score -> {player_score}\n"
        f"CPU Score -> {cpu_score}\n"
        f"Draw Score -> {draw_score}"
    )
    if player_score > cpu_score:
        return (
            f"{WON_MESSAGE}\n"
            f"{baseline_scoreboard}"
        )
    if cpu_score > player_score:
        return (
            f"{LOST_MESSAGE}\n"
            f"{baseline_scoreboard}"
        )
    return (
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
        for _ in range(NUMBER_ROUNDS):
            scores = game_logic()
            if scores is None:
                break
            PLAYER, CPU, DRAW = map(
                    lambda score: sum(score),
                    zip((PLAYER, CPU, DRAW), scores)
                )
        if not scores is None:
            # print(PLAYER, CPU, DRAW)
            print(f"\n{final_scores(PLAYER, CPU, DRAW)}")
        break


if __name__ == '__main__':
    main()
