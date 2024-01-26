import keyboard
import webbrowser

def hotkey_pressed():
    print("noob!")
    webbrowser.open('https://www.youtube.com/watch?v=uHgt8giw1LY')

keyboard.add_hotkey('space', hotkey_pressed)
keyboard.wait()
