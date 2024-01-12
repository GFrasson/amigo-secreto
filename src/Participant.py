class Participant:
  def __init__(self, participant_subscription: str):
    participant_subscription_splitted = participant_subscription.split(',')
    self.__name = participant_subscription_splitted[0]
    self.__email = participant_subscription_splitted[1].strip() if len(participant_subscription_splitted) > 1 else None
    self.__secret_friend: Participant = None
    self.__is_taken = False

  @property
  def name(self):
    return self.__name
  
  @property
  def email(self):
    return self.__email
  
  @property
  def secret_friend(self):
    return self.__secret_friend
  
  @property
  def is_taken(self):
    return self.__is_taken
  
  @name.setter
  def name(self, name):
    self.__name = name

  @email.setter
  def email(self, email):
    self.__email = email
  
  @secret_friend.setter
  def secret_friend(self, secret_friend):
    self.__secret_friend = secret_friend
  
  @is_taken.setter
  def is_taken(self, is_taken):
    self.__is_taken = is_taken
  