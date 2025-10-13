import speech_recognition as sr
import os

def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        if '종료' in text:
            print('종료합니다.')
            stop(wait_for_stop=False)
            os._exit(0)
        print('[홍길동]' + text)
    except sr.UnknownValueError:
        print('인식 실패')

    except sr.RequestError:
        print('요청 실패')


print('말씀하세요!')
mic = sr.Microphone()
stop=sr.Recognizer().listen_in_background(mic, listen)

while True:
    pass