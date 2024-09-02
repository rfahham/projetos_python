from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = "Hello World", lang= language, slow=False)

sp.save(audio)
playsound(audio)