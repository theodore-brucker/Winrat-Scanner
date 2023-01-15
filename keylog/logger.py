import keyboard as Keys

#Tracks all keyboard events until = is pressed down
keyboardLog = Keys.record(until = '=')
print(keyboardLog)