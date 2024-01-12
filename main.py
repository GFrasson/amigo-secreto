from dotenv import load_dotenv
from os import path, mkdir, getenv
from datetime import datetime
from src.SecretFriend import SecretFriend
from src.Participant import Participant
from src.EmailProvider import EmailProvider


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


def send_emails(participants: list[Participant]):
  email_provider = None
  
  try:
    email_provider = EmailProvider(email_from=getenv('EMAIL_FROM'), email_password=getenv('EMAIL_PASSWORD'))
  except Exception as error:
    print(error)
    return

  for participant in participants:
    if participant.email is None:
      continue
    
    message = email_provider.add_email_message(
      email_to=participant.email,
      name_from='Amigo Secreto',
      subject='Sorteio Amigo Secreto'
    )
    email_provider.set_template(
      template_path=path.join(path.curdir, 'templates', 'email-template.html'),
      message=message,
      name=participant.name,
      secret_friend=participant.secret_friend.name
    )

  email_provider.send_emails()


if __name__ == '__main__':
  load_dotenv()

  participants_names: list[str] = read_participants('participants.txt')

  secrect_friend = SecretFriend(participants_names)
  participants = secrect_friend.raffle()

  for participant in participants:
    print(f'{participant.name} -> {participant.secret_friend.name}')

  write_results_on_files(participants)
  send_emails(participants)
