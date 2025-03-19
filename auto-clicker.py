import pyautogui
import time
from PIL import ImageGrab
import win32api
import win32con
from pynput import keyboard
import threading

# Target color in RGB (convert #0866FF to RGB)
TARGET_COLOR = (8, 102, 255)
running = False
program_running = True

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def get_mouse_position():
    return win32api.GetCursorPos()

def check_color():
    x, y = get_mouse_position()
    area = (x-2, y-2, x+3, y+3)
    screenshot = ImageGrab.grab(area)
    
    for px in range(screenshot.width):
        for py in range(screenshot.height):
            if screenshot.getpixel((px, py)) == TARGET_COLOR:
                return True
    return False

def on_press(key):
    global running, program_running
    try:
        if key == keyboard.Key.f6:
            running = not running
            if running:
                print("Auto-clicker started! Press F6 to pause, F7 to exit.")
            else:
                print("Auto-clicker paused! Press F6 to resume.")
        elif key == keyboard.Key.f7:
            print("\nAuto-clicker stopped!")
            program_running = False
            return False
    except:
        pass

def clicker():
    global running, program_running
    while program_running:
        if running:
            if check_color():
                x, y = get_mouse_position()
                click(x, y)
                time.sleep(0.5)  # Prevent multiple clicks
            time.sleep(0.1)  # Reduce CPU usage
        else:
            time.sleep(0.1)

print("Press F6 to start/pause the auto-clicker")
print("Press F7 to exit the program")
print("Looking for color: #0866FF")

# Start the keyboard listener in a separate thread
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Start the clicker in the main thread
clicker()