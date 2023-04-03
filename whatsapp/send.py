#!/usr/bin/env python
#-*- coding: utf-8 -*-

import emoji
import pywhatkit
import time
from datetime import datetime

# contatos = ['+55 22981119538', '+55 21980025474', '+55 21981836521']
contatos = ['+55 21980025474']
mensagem = emoji.emojize("😀")
print(mensagem)

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], mensagem, datetime.now().hour,datetime.now().minute +1)
    time.sleep(3)