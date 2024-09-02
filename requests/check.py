import urllib.request
# import pyttsx3 // https://pyttsx3.readthedocs.io/en/latest/engine.html
from time import sleep

# voice = pyttsx3.init()

link = 'https://google.com'

def connect():
    try:
        req = urllib.request.urlopen(link)
        print(req.status)
        return True
    
    except:
        return False
    
while True:
    if connect():
        print("Connected !")
        # voice.say("Connected")
    else:
        print("Error - Not Connected !")
        
    sleep(5)