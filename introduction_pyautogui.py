import pyautogui

# get width and height of your screen
width, height= pyautogui.size()
width
height

# get current position of courser
# top left corner is 0,0
# Note: in programming, Y-coordinates increase when going down!
pyautogui.position()

# move courser to specific coordinate
pyautogui.moveTo(30,30)
pyautogui.moveTo(30,30, duration= 3) # slow down movement

# move relative to where the courser already is
pyautogui.moveRel(200,0) # move 200 to the right
pyautogui.moveRel(200,0, duration=2) 

pyautogui.moveRel(0,-100, duration=2) # move up

#Specifiy the position you want to click on:
pyautogui.position()
# then click it
pyautogui.click(565,25)
#double click
pyautogui.doubleClick(565,25)
# right click
pyautogui.rightClick(565,25)
# middle click
pyautogui.middleClick(565,25)

# get real time position of courser:
# In terminal: 
# import pyautogui 
# pyautogui.displayMousePosition()
