class Participant:
  def __init__(self, name: str):
    self.__name = name
    self.__secret_friend: Participant = None
    self.__is_taken = False

  @property
  def name(self):
    return self.__name
  
  @property
  def secret_friend(self):
    return self.__secret_friend
  
  @property
  def is_taken(self):
    return self.__is_taken
  
  @name.setter
  def name(self, name):
    self.__name = name
  
  @secret_friend.setter
  def secret_friend(self, secret_friend):
    self.__secret_friend = secret_friend
  
  @is_taken.setter
  def is_taken(self, is_taken):
    self.__is_taken = is_taken
  