import pyautogui

pyautogui.click()
# type and set time
pyautogui.typewrite('Hello World', interval=0.2)

#type and move back
pyautogui.typewrite(['a','b','left','left','X','Y'], interval=1)

# find more of these string names
pyautogui.KEYBOARD_KEYS

#pyautogui.press('f1')

# press series of keys in combination
pyautogui.hotkey('ctrl', 'o')