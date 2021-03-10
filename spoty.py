import webbrowser, time
import pyautogui as robot

user= "user"
pword="password"

# Go to Google
webbrowser.open("https://google.com")
time.sleep(2)

# Go to Spotify
robot.typewrite("https://open.spotify.com/browse/featured?_ga=2.258604426.105587266.1519520067-2109950989.1509753104")
time.sleep(0.5)
robot.press('enter')
time.sleep(9)

# Keyboard commands
commands= list(user+pword)
commands.insert(len(user),"tab")
commands.extend(['tab', 'tab', 'tab', 'enter'])
# Click - Log in
robot.typewrite(['tab', 'tab', 'enter'],interval=0.1)
time.sleep(4)

# Login in
robot.hotkey('ctrl', 'a')
robot.typewrite(commands,interval=0.1)

# Load page & Play
time.sleep(11)
robot.hotkey("space")



