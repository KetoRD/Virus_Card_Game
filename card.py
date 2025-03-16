class Card:

  def __init__(self, card_type: str, color: str):
    self.card_type = card_type
    self.color = color
    self.num_medicine_cards = 0
    self.num_virus_cards = 0
    
  def get_name(self):
    if self.num_medicine_cards > 0:
      return f"Card [{self.card_type} - {self.color} ({'Vaccinated' if self.num_medicine_cards == 1 else 'Immunised'})]"
    
    elif self.num_virus_cards > 0:
      return f"Card [{self.card_type} - {self.color} ({'Infected'})]"
    
    else:
      return f"Card: [{self.card_type} - {self.color}]"

  def __str__(self):
    return self.get_name()

  def __repr__(self):
    return str(self)