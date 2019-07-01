import pyautogui

# take screenshoot and save it
pyautogui.screenshot('C:/Analysen/automatization/example.png')

# image recognition: output is the position of button incl- the hight and with of the image
pyautogui.locateOnScreen('C:/Analysen/automatization/Rechner/key_2.png') 

# image recognition: output is the center position of button
pyautogui.locateCenterOnScreen('C:/Analysen/automatization/Rechner/key_2.png')   

# use calculator
key_2=pyautogui.locateCenterOnScreen('C:/Analysen/automatization/Rechner/key_2.png')  
pyautogui.moveTo(key_2, duration=1)
pyautogui.click(key_2)

key_cross=pyautogui.locateCenterOnScreen('C:/Analysen/automatization/Rechner/key_cross.png')  
pyautogui.moveTo(key_cross, duration=1)
pyautogui.click(key_cross)

key_seven=pyautogui.locateCenterOnScreen('C:/Analysen/automatization/Rechner/key_7.png')  
pyautogui.moveTo(key_seven, duration=1)
pyautogui.click(key_seven)

key_equal=pyautogui.locateCenterOnScreen('C:/Analysen/automatization/Rechner/key_equal.png')  
pyautogui.moveTo(key_equal, duration=1)
pyautogui.click(key_equal)
