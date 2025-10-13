from gtts import gTTS
from playsound import playsound

file_name = 'data/sample3.mp3'
with open('data/sample_en.txt') as file:
    text = file.read()
print(text)

tts_en = gTTS(text=text, lang='en')
tts_en.save(file_name)
playsound(file_name)