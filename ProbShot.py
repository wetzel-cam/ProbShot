# Inspired by this video:
# 'Surviving The Deadliest Two-Player Game'
# https://youtu.be/ACtsYN1TWLg

# Native Modules
# import sys

# 3rd-Party Modules
# import pygame

# Personal Modules
from Player import Player

shots_per_round = {}

# Main game loop
# Only made for running two players; needs to be adapted for 2 or more players
def run(runs=100, output_wins=False, modified_game=False):
    run_count = 0
    # The loop for each game to be ran
    while run_count < runs:
        # Resets counts
        reset()
        shots_taken = 0
        winner = None

        # The game loop for each round
        if modified_game:
            while True:
                # Begin the player's turn
                for player in Player.active_players.values():
                    x = 0

                    # Allows the player to shoot +1 from previous round
                    while x < shots_taken + 1:
                        player.take_shot()

                        # Win condition for round
                        if not player.enemy.alive:
                            player.tally_win()
                            winner = player.name

                            if output_wins:
                                print(player.name, "wins")

                            break
                        x += 1

                    shots_taken = x
                    # print(shots_taken)
                    if winner != None:
                        break
                if winner != None:
                    break
        else:
            while True:
                for player in Player.active_players.values():
                    shots_taken += 1
                    player.take_shot()

                    if not player.enemy.alive:
                        player.tally_win()
                        winner = player.name

                        if output_wins:
                            print(player.name, "wins")

                        break

                if winner != None:
                    break

        log_shots(shots_taken)

        run_count += 1

# Resets all counts
def reset():
    for player in Player.active_players.values():
        player.reset()

# Compiles a list of the amount of shots it took per round
def log_shots(shots):
    global shots_per_round

    try:
        shots_per_round[shots] += 1
    except KeyError as e:
        shots_per_round[shots] = 1

    order_shots()

# Orders the shots_per_round to make it all pretty
def order_shots():
    global shots_per_round

    ordered_dict = {}

    for i in sorted(shots_per_round.keys()):
        ordered_dict[i] = shots_per_round[i]

    shots_per_round = ordered_dict

def parse_input(user_input):
    if user_input.lower() == "true":
        return True
    else:
        return False

if __name__ == "__main__":
    Player.define_players(2)

    player1 = Player.active_players["Player 1"]
    player2 = Player.active_players["Player 2"]

    player1.enemy = player2
    player2.enemy = player1

    try:
        games = int(input("Amount of games to run (default is 100): "))
    except ValueError as e:
        print("No number was passed as input, using default value")
        games = 100

    output_wins = parse_input(input("Output wins (default is False): "))
    modified_game = parse_input(input("Modified game (default is False): "))

    run(games, output_wins, modified_game)

    for player in Player.active_players.values():
        print(player, "won", player.wins, "times")

    print(shots_per_round)