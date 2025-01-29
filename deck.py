import random
from card import Card

class Deck:

  def __init__(self):
    self.deck = []
    self.discard_pile = []

    self.add_cards_to_deck('Organ', 5, 1, False, 0)
    self.add_cards_to_deck('Virus', 4, 1, False, 0)
    self.add_cards_to_deck('Medicine', 4, 4, False, 0)
    self.add_cards_to_deck('Treatment - Transplant', 0, 0, True, 2)
    self.add_cards_to_deck('Treatment - Organ Thief', 0, 0, True, 3)
    self.add_cards_to_deck('Treatment - Contagion', 0, 0, True, 3)
    self.add_cards_to_deck('Treatment - Latex Glove', 0, 0, True, 1)
    self.add_cards_to_deck('Treatment - Medical Error', 0, 0, True, 1)

    random.shuffle(self.deck)

  def add_cards_to_deck(self, card_type, num_cards_color, num_cards_multi_color, treatment_status, num_cards_treatment):

    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Multi-Color']
    treatments = ['Transplant', 'Organ Thief', 'Contagion', 'Latex Glove', 'Medical Error']

    for cards_deck in colors:
      if cards_deck == 'Multi-Color':
        for card in range(num_cards_multi_color):
          self.deck.append(Card(card_type, cards_deck))
      else:
        for card in range(num_cards_color):
          self.deck.append(Card(card_type, cards_deck))

    if treatment_status == True:
      for cards_deck in range(num_cards_treatment):
        self.deck.append(Card(card_type, ""))


  def draw_card_from_deck(self, player, num_cards_to_take):
    for card in range(num_cards_to_take):
      player.player_hand.append(self.deck[0])
      self.deck.pop(0)

  def put_card_on_discard_pile(self, player, card_idx):
    self.discard_pile.append(player.player_hand[card_idx])
    player.player_hand.pop(card_idx)