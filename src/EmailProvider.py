from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


class EmailProvider:
  def __init__(self, email_from: str, email_password: str):
    if not email_from or not email_password:
      raise Exception('Email or password missing.')

    self.email_from = email_from
    self.email_password = email_password
    self.messages: list[MIMEMultipart] = []

  def add_email_message(self, email_to: str, name_from: str, subject: str) -> MIMEMultipart:
    message = MIMEMultipart('alternative')
    message['from'] = name_from
    message['to'] = email_to
    message['subject'] = subject

    self.messages.append(message)

    return message

  def set_template(self, template_path, message: MIMEMultipart, **kwargs):
    with open(template_path, 'r', encoding='utf8') as file:
      template = Template(file.read())
      message_body = template.substitute(kwargs)

      body = MIMEText(message_body, 'html')
      message.attach(body)

  def attach_image(self, image_path, message: MIMEMultipart):
    with open(image_path, 'rb') as img:
      img = MIMEImage(img.read())
      message.attach(img)

  def send_emails(self):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
      try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.email_from, self.email_password)

        for message in self.messages:
          smtp.send_message(message)
          print('E-mail enviado com sucesso.')
      except Exception as e:
        print('E-mail não pôde ser enviado...')
        print('Erro:', e)
