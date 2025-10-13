import speech_recognition as sr

with sr.Microphone() as source:
    print('듣고있어요.')
    audio = sr.Recognizer().listen(source)

text = sr.Recognizer().recognize_google(audio, language='ko')
print(text)