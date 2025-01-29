from player import Player

class GameMaster:
  def __init__(self):
    pass

  def start_game(self):
    self.players = []

    print("Virus! The most contagious card game")
    print("")

    while True:
      self.num_players = int(input("Type the number of players (2-6): "))
      if self.num_players < 2 or self.num_players > 6:
        print("Error, number of players out of range. Try again")
        continue
      else:
        for player in range(self.num_players):
          player_name = input(f"Enter name for player {player + 1} ")
          self.players.append(Player(player_name))
      print("Players added successfully!")
      print(self.players)