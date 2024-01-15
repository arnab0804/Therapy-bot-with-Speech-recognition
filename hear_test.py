from gtts import gTTS
from playsound import playsound

text='Who are you?'
lang='en'
tld='co.uk'

audio_obj=gTTS(text=text,lang=lang,slow=False,tld='co.uk')
audio_obj.save('intro.mp3')

playsound('intro.mp3')