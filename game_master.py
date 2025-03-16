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
      #print("Players added successfully!")
      #print(self.players)

      ##################################################################################################################

      deck = Deck()

      for player in range(self.num_players):
        deck.draw_card_from_deck(self.players[player], 3)

      #print("3 cards have been distributed to all players")

      virus_game = True

      while virus_game:
        current_player_idx = self.total_turns % self.num_players
        current_player_turn = self.players[current_player_idx]

        print(f"Player's turn: {current_player_turn}")
        print(f"This is your current hand: {self.players[current_player_idx].player_hand}\n")

        print("These are the bodies: ")
        for player in range(self.num_players):
          print(f"{player + 1}. {self.players[player]}'s body: {self.players[player].player_body}")
        print("")

        option = int(input("Select an option:\n 1. Play a card\n 2. Discard a card\n 3. Next turn\n"))

        if option == 1:
          if len(self.players[current_player_idx].player_hand) == 3:
            card_idx = int(input("Select a card from your hand: "))
            card_idx -= 1
            card_selected = self.players[current_player_idx].player_hand[card_idx]
            print(f"Card selected: {card_selected}")

            body_idx_to_put_card = int(input("Type body's player number to place card on: "))
            body_idx_to_put_card -= 1
            
            if card_selected.card_type == "Organ":
              if body_idx_to_put_card != current_player_idx:
                print("You can only place an organ on your own body")
                continue
              
            elif card_selected.card_type == "Medicine":
              if body_idx_to_put_card != current_player_idx:
                print("You can only place a medicine on your own body")
                continue
              
            elif card_selected.card_type == "Virus":
              if body_idx_to_put_card == current_player_idx:
                print("You cannot place a virus on your own body")
                continue

            if card_selected.card_type == "Medicine":
              for player_card in self.players[body_idx_to_put_card].player_body:
                if player_card.color == card_selected.color:
                  if player_card.num_virus_cards == 1:
                    player_card.num_virus_cards -= 1
                    self.players[current_player_idx].player_hand.pop(card_idx)
                  elif player_card.num_virus_cards == 0:
                    player_card.num_medicine_cards += 1
                    self.players[current_player_idx].player_hand.pop(card_idx)
                  
            if card_selected.card_type == "Virus":
              for player_card in self.players[body_idx_to_put_card].player_body:
                if player_card.color == card_selected.color:
                  if player_card.num_medicine_cards == 1:
                    player_card.num_medicine_cards -= 1
                    self.players[current_player_idx].player_hand.pop(card_idx)
                  elif player_card.num_medicine_cards == 0:
                    player_card.num_virus_cards += 1
                    self.players[current_player_idx].player_hand.pop(card_idx)
            
            if card_selected.card_type != "Medicine" and card_selected.card_type != "Virus":
              self.players[body_idx_to_put_card].player_body.append(card_selected)
              self.players[current_player_idx].player_hand.pop(card_idx)
              print("This is the error")

            cards_to_add = 3 - len(self.players[current_player_idx].player_hand)
            deck.draw_card_from_deck(self.players[current_player_idx], cards_to_add)

            self.total_turns += 1
            continue

          else:
            print(f"This move is not possible. You have already discarded {3-len(self.players[current_player_idx].player_hand)} cards")
            continue

        elif option == 2:
          if len(self.players[current_player_idx].player_hand) == 0:
            print("Your turn is over, you have no cards left to discard")

            # When a player's turn is over, this checks how many cards were played, and therefore how many are needed to
            # be added to the player's hand
            cards_to_add = 3 - len(self.players[current_player_idx].player_hand)
            deck.draw_card_from_deck(self.players[current_player_idx], cards_to_add)

            # This moves the turn to the next player
            self.total_turns += 1
            continue

          else:
            card_idx = int(input("Select a card from your hand to discard: "))
            card_idx -= 1
            card_selected = self.players[current_player_idx].player_hand[card_idx]
            print(f"Card selected to discard: {card_selected}")

            deck.discard_pile.append(card_selected)
            self.players[current_player_idx].player_hand.pop(card_idx)
            print(f"Total cards in discard pile: {len(deck.discard_pile)}")
            continue

        elif option == 3:
          if len(self.players[current_player_idx].player_hand) == 3:
            print("Invalid option. You have to make a move first")
          else:
            cards_to_add = 3 - len(self.players[current_player_idx].player_hand)
            deck.draw_card_from_deck(self.players[current_player_idx], cards_to_add)

            self.total_turns += 1
            continue

