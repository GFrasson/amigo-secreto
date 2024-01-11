from os import path, mkdir
from datetime import datetime
from src.SecretFriend import SecretFriend
from src.Participant import Participant


def read_participants(file_name):
  participants_names: list[str] = None
  with open(file_name, 'r') as file:
    participants_names = file.read().splitlines()

  return participants_names


def write_results_on_files(participants: list[Participant]):
  output_folder_path = path.join(path.curdir, 'output')
  if not path.isdir(output_folder_path):
    mkdir(output_folder_path)

  raffle_folder_path = path.join(output_folder_path, datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
  mkdir(raffle_folder_path)

  for participant in participants:
    with open(path.join(raffle_folder_path, f'{participant.name}.txt'), 'w') as file:
      file.write(f'{participant.name.title()}, seu amigo secreto é: {participant.secret_friend.name.title()}!!!')


if __name__ == '__main__':
  participants_names: list[str] = read_participants('participants.txt')

  secrect_friend = SecretFriend(participants_names)
  participants = secrect_friend.raffle()

  for participant in participants:
    print(f'{participant.name} -> {participant.secret_friend.name}')

  write_results_on_files(participants)
