from player import Player
from deck import Deck

class GameMaster:
  def __init__(self):
    pass

  def start_game(self):
    self.players = []
    self.total_turns = 0

    print("Virus! The most contagious card game")
    print("")

    collect_players = False

    while not collect_players:
      self.num_players = int(input("Type the number of players (2-6): "))
      if self.num_players < 2 or self.num_players > 6:
        print("Error, number of players out of range. Try again")
        continue
      else:
        for player in range(self.num_players):
          player_name = input(f"Enter name for player {player + 1}: ")
          self.players.append(Player(player_name))
          collect_players = True
      print("Players added successfully!")
      print(self.players)

      ##################################################################################################################

      deck = Deck()

      for player in range(self.num_players):
        deck.draw_card_from_deck(self.players[player], 3)

      print("3 cards have been distributed to all players")

      virus_game = True

      while virus_game:
        current_player_idx = self.total_turns % self.num_players
        current_player_turn = self.players[current_player_idx]

        print(f"Player's turn: {current_player_turn}")
        print("")

        print(f"This is your current hand: {self.players[current_player_idx].player_hand}")
        print("")

        print("These are the bodies: ")
        for player in range(self.num_players):
          print(f"{self.players[player]}'s body: {self.players[player].player_body}")
        print("")

        option = int(input("Select an option:\n 1. Play cards\n 2. Skip\n"))

        if option == 1:
          print("Awesome! Let's play!")
          break
        elif option == 2:
          self.total_turns += 1
          continue

