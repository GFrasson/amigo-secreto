from src.Participant import Participant
import random


def include_participant_left(participants: list[Participant], participant_left: Participant):
  participants_with_secret_friend = [participant for participant in participants if participant.secret_friend is not None]
  random_participan_list = random.sample(participants_with_secret_friend, k=1)

  if len(random_participan_list) == 0:
    return
  
  random_participant = random_participan_list[0]

  secret_friend_aux = random_participant.secret_friend

  random_participant.secret_friend = participant_left
  participant_left.is_taken = True
  
  participant_left.secret_friend = secret_friend_aux


def get_not_taken_participants(participants: list[Participant]):
  return [participant for participant in participants if participant.is_taken == False]


def get_participants_without_friend(participants: list[Participant]):
  return [participant for participant in participants if participant.secret_friend is None]


def take_secret_friend(participants):
  if len(participants) == 0:
    return None
  
  taken_participant: Participant = random.sample(participants, k=1)[0]
  taken_participant.is_taken = True

  return taken_participant


if __name__ == '__main__':
    participants: list[Participant] = None

    with open('participants.txt', 'r') as file:
      participants = [Participant(participant_name) for participant_name in file.read().splitlines()]

    participants_left = get_participants_without_friend(participants)

    while len(participants_left) > 0:
      for current_participant in participants_left:
        not_taken_participants = get_not_taken_participants(participants)
        participants_options_to_take = [participant for participant in not_taken_participants if participant != current_participant]
                
        current_participant.secret_friend = take_secret_friend(participants_options_to_take)

      participants_left = get_participants_without_friend(participants)

      if len(participants_left) > 0:
        include_participant_left(participants, participants_left[0])
        participants_left = get_participants_without_friend(participants)
