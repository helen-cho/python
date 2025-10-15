import pyautogui

window = pyautogui.getWindowsWithTitle('제목 없음')[0]
window.activate()

pyautogui.write('12345')
pyautogui.write(['T', 'E', 'S', 'T', 'left', 'left', '-', 'right', 'right', 'enter'])

# pyautogui.keyDown('shift')
# pyautogui.press('4')
# pyautogui.keyUp('shift')
#pyautogui.hotkey('shift', '4')

for i in range(2):
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.write(['right'])
    pyautogui.hotkey('ctrl', 'v')

window.close()
pyautogui.write('n')