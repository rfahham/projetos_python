import os
import smtplib
import threading
from getpass4 import getpass
from time import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from threading import Timer

cores = {'vermelho':'\033[31m','verde':'\033[32m',}
hostname = "glodsdsdbo.com"
response = os.system("ping -c 1 " + hostname)
# beep = os.system( "say Vamos testar !!!" )

def enviar_email():
	
	email = "rfahham@hotmail.com"
	password = getpass('Digite sua senha: ')
	password = ""
	send_to_email = "rfahham@hotmail.com"
	subject = "Teste de conexão com o servidor"
	message = "O servidor parou de responder!"
		
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = send_to_email
	msg['Subject'] = subject
		
	msg.attach(MIMEText(message, 'html'))
	
	server = smtplib.SMTP_SSL('SMTP.office365.com', 465)
	server.login(email, password)
	text = msg.as_string()
	server.sendmail(email, send_to_email, text)
	server.quit()

def validar():
	if response == 0:
		print("")
		print('\033[32mServer is UP !!!\033[m ')
	else:
		enviar_email()
		print('\033[31mServer is DOWN !!!\033[m ')
		# beep
	sleep(10)

while True:
	validar()