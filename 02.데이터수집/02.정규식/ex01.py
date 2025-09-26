#정규식
import re

pattern = re.compile('ca.e')
while True:
    word = input('단어>')
    if word=='': break

    match = pattern.match(word)
    if match:
        print('일치')
    else:
        print('불일치')