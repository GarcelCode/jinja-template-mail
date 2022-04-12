from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from jinja2 import Environment, FileSystemLoader
import os

from data_files.data_errormail import data_file_filled, data_file_partial, data_file_empty, data_without_user
from data_files.data_efosmail import efos_data_file_filled
from data_files.data_confirmmail import confirm_data
from data_files.data_temporarypass import data_pass
from data_files.efirma_mail import efirma_data
from globals import g_to_email, g_from_email, g_password_email

env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))

def get_data():
    data = data_pass
    return data

def send_mail(bodyContent):
    to_email = g_to_email
    from_email = g_from_email
    subject = '4 restablecer contraseña'
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = to_email

    message.attach(MIMEText(bodyContent, 'html'))
    msgBody = message.as_string()

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, g_password_email)
    server.sendmail(from_email, to_email, msgBody)
    server.quit()

def send_movie_list():
    json_data = get_data()
    template = env.get_template('solcp-change-password.html')
    bodyContent = template.render(json_data)
    send_mail(bodyContent)
    return "Mail sent successfully"

send_movie_list()