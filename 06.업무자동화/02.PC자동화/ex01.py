import pyautogui

# pyautogui.sleep(2)
# p=pyautogui.position()
# print(p)

#pyautogui.sleep(2)
#pyautogui.moveTo(3324, 169, duration=2)
#pyautogui.click(3324, 169, duration=2)

#pyautogui.mouseInfo()

# pyautogui.sleep(2)
# print(pyautogui.position())

# pyautogui.moveTo(1952, 127, duration=0.5)
# pyautogui.move(100, 100, duration=0.5)
# pyautogui.move(100, 100, duration=0.5)


# pyautogui.sleep(2)
# print(pyautogui.position())

pyautogui.sleep(2)
try:
    manage = pyautogui.locateOnScreen('data/logo.png')
    print(manage)
    pyautogui.click(manage)
except Exception:
    print('찾지못함.')

# p = pyautogui.position()
# pyautogui.click(p.x, p.y)

# pyautogui.moveTo(p.x, p.y, duration=0.5)
# pyautogui.drag(100, 100, duration=0.5)