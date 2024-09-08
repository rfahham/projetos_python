import smtplib

# GMAIL

# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.ehlo()
# response = server.ehlo_resp
# print(response)

# OUTLOOK
try:
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
except Exception as e:
    print(e)
    server = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
server.ehlo()
response = server.ehlo_resp
print(response)