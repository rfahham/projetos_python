import smtplib

# GMAIL

# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.ehlo()
# response = server.ehlo_resp
# print(response)

# OUTLOOK
try:
    server = smtplib.SMTP('smtp.office365.com', 587)
except Exception as e:
    print(e)
    server = smtplib.SMTP_SSL('smtp.office365.com', 465)
server.ehlo()
response = server.ehlo_resp
print(response)