import smtplib
from email.mime.text import MIMEText

subject = "Assunto do Email"
body = "Este é o corpo da mensagem"
sender = "rfahham@gmail.com"
recipients = ["rfahham@gmail.com", "rfahham@hotmail.com"]
password = ""

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Mensagem enviada!")

send_email(subject, body, sender, recipients, password)