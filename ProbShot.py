# Inspired by this video:
# 'Surviving The Deadliest Two-Player Game'
# https://youtu.be/ACtsYN1TWLg

# Native Modules
# import sys

# 3rd-Party Modules
# import pygame

# Personal Modules
from Player import Player

shotsPerRound = {}

# Main game loop
# Only made for running two players; needs to be adapted for 2 or more players
def run(runs, outputWins=False, improvedGame=False):
    runCount = 0
    # The loop for each game to be ran
    while runCount < runs:
        # Resets counts
        reset()
        shotsTaken = 0
        winner = None

        # The game loop for each round
        if improvedGame:
            while True:
                # Begin the player's turn
                for player in Player.activePlayers.values():
                    x = 0

                    # Allows the player to shoot +1 from previous round
                    while x < shotsTaken + 1:
                        player.takeShot()

                        # Win condition for round
                        if not player.enemy.alive:
                            player.tallyWin()
                            winner = player.name

                            if outputWins:
                                print(player.name, "wins")

                            break
                        x += 1

                    shotsTaken = x
                    # print(shotsTaken)
                    if winner != None:
                        break
                if winner != None:
                    break
        else:
            while True:
                for player in Player.activePlayers.values():
                    shotsTaken += 1
                    player.takeShot()

                    if not player.enemy.alive:
                        player.tallyWin()
                        winner = player.name

                        if outputWins:
                            print(player.name, "wins")

                        break

                if winner != None:
                    break

        logShots(shotsTaken)

        runCount += 1

# Resets all counts
def reset():
    for player in Player.activePlayers.values():
        player.reset()

# Compiles a list of the amount of shots it took per round
def logShots(shots):
    global shotsPerRound

    try:
        shotsPerRound[shots] += 1
    except KeyError as e:
        shotsPerRound[shots] = 1

    orderShots()

# Orders the shotsPerRound to make it all pretty
def orderShots():
    global shotsPerRound

    orderedDict = {}

    for i in sorted(shotsPerRound.keys()):
        orderedDict[i] = shotsPerRound[i]

    shotsPerRound = orderedDict

if __name__ == "__main__":
    Player.definePlayers(2)

    player1 = Player.activePlayers["Player 1"]
    player2 = Player.activePlayers["Player 2"]

    player1.enemy = player2
    player2.enemy = player1

    run(100000, False, True)

    for player in Player.activePlayers.values():
        print(player, "won", player.wins, "times")

    print(shotsPerRound)