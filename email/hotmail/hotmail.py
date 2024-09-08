import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

# Configurações do e-mail e credenciais de login
outlook_server = 'smtp-mail.outollok.com'
outlook_port = 465
outlook_user = 'rfahham@hotmail.com'
outlook_password = ''

# Destinatário e remetente
sender = outlook_user
recipient = 'rfahham@hotmail.com'

# Assunto e corpo do e-mail
subject = 'Teste de envio de E-mail'
body = 'Aqui está o arquivo em anexo.'

# Caminho do arquivo que será anexado
file_path = './planilha.xlsx'
file_name = 'planilha.xlsx'

# Criação da mensagem de e-mail
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject

# Anexa o corpo do e-mail
msg.attach(MIMEText(body, 'plain'))

# Lê o arquivo que será anexado
with open(file_path, 'rb') as file:
    file_data = file.read()

# Cria a parte MIMEApplication para o arquivo em anexo
part = MIMEApplication(file_data, _subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet")
part.add_header('Content-Disposition', f'attachment; filename="{file_name}"')

# Anexa o arquivo ao e-mail
msg.attach(part)

# Envia o e-mail através do servidor SMTP do Outlook
try:
    with smtplib.SMTP_SSL(outlook_server, outlook_port) as server:
        server.ehlo()
        server.starttls()
        server.login(outlook_user, outlook_password)
        server.send_message(msg)
        print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
