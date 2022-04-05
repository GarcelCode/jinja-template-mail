from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from jinja2 import Environment, FileSystemLoader
import os

from data import data_file


env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))

def get_data():
    data = data_file
    return data

def send_mail(bodyContent):
    to_email = 'garcelcode@gmail.com'
    from_email = 'testmail.gcdev@gmail.com'
    subject = 'CFDIS con errores reporte mensual'
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = to_email

    message.attach(MIMEText(bodyContent, 'html'))
    msgBody = message.as_string()

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, '@Gogl/test;')
    server.sendmail(from_email, to_email, msgBody)
    server.quit()

def send_movie_list():
    json_data = get_data()
    template = env.get_template('child.html')
    bodyContent = template.render(data=json_data)
    send_mail(bodyContent)
    return "Mail sent successfully"

send_movie_list()