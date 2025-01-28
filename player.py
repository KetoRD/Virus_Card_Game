class Player:

  def __init__(self, name):
    self.name = name
    self.player_hand = []
    self.player_body = []

  def get_name(self):
    return self.name

  def __str__(self):
    return self.get_name()

  def __repr__(self):
    return str(self)