class Card:

  def __init__(self, card_type: str, color: str):
    self.card_type = card_type
    self.color = color

  def get_name(self):
    return f"Card: [{self.card_type} - {self.color}]"

  def __str__(self):
    return self.get_name()

  def __repr__(self):
    return str(self)