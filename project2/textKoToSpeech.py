from gtts import gTTS
from playsound import playsound

file_name = 'data/sample2.mp3'
text = '파이썬을 배우면 이런것도 할 수 있어요.'
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)