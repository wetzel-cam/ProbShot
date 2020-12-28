from random import randint as rand

class Player:
    active_players = {}

    @staticmethod
    def define_players(count):
        i = 0
        while i < count:
            Player("Player " + str(i+1))
            i += 1

    @staticmethod
    def _add_player(name, player_object):
        Player.active_players[name] = player_object

    def __init__(self, name):
        self._name = name
        self._shots = 0
        self._alive = True
        self._wins = 0
        self._enemy = None

        Player._add_player(self._name, self)

    def __str__(self):
        return self._name

    def take_shot(self):
        chamber = rand(1, 6)

        self._shots += 1

        if chamber == 1:
            self._enemy.alive = False

    def tally_win(self):
        self._wins += 1
    
    def reset(self):
        self._alive = True
        self._shots = 0

    @property
    def name(self):
        return self._name

    @property
    def enemy(self):
        return self._enemy
    
    @enemy.setter
    def enemy(self, player):
        self._enemy = player
    
    @property
    def wins(self):
        return self._wins

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, status):
        self._alive = status

    @property
    def shots(self):
        return self._shots

    