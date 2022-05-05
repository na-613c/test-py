import pyautogui

path = 'IMG/03.png'
pyautogui.sleep(5)
button = pyautogui.locateOnScreen(path, grayscale=True, confidence=0.7)
pyautogui.doubleClick(button)

print('hello word')
