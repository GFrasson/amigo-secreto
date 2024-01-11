import random
from src.Participant import Participant


class SecretFriend:
  def __init__(self, participants_names: list[str]):
    self.participants = [Participant(participant_name) for participant_name in participants_names]
  
  def raffle(self):
    participants_left = self.get_participants_without_friend()

    while len(participants_left) > 0:
      for current_participant in participants_left:
        not_taken_participants = self.get_not_taken_participants()
        participants_options_to_take = [participant for participant in not_taken_participants if participant != current_participant]
                
        current_participant.secret_friend = self.take_secret_friend(participants_options_to_take)

      participants_left = self.get_participants_without_friend()

      if len(participants_left) > 0:
        self.include_participant_left(participants_left[0])
        participants_left = self.get_participants_without_friend()
    
    return self.participants

  def include_participant_left(self, participant_left: Participant):
    participants_with_secret_friend = [participant for participant in self.participants if participant.secret_friend is not None]
    random_participan_list = random.sample(participants_with_secret_friend, k=1)

    if len(random_participan_list) == 0:
      return
    
    random_participant = random_participan_list[0]

    secret_friend_aux = random_participant.secret_friend

    random_participant.secret_friend = participant_left
    participant_left.is_taken = True
    
    participant_left.secret_friend = secret_friend_aux

  def get_not_taken_participants(self):
    return [participant for participant in self.participants if participant.is_taken == False]

  def get_participants_without_friend(self):
    return [participant for participant in self.participants if participant.secret_friend is None]

  def take_secret_friend(self, participants):
    if len(participants) == 0:
      return None
    
    taken_participant: Participant = random.sample(participants, k=1)[0]
    taken_participant.is_taken = True

    return taken_participant
