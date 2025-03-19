# Color Detection Auto-Clicker

A Python auto-clicker that automatically clicks when it detects a specific color (#0866FF) under the mouse cursor.

## Features

- Color detection (#0866FF - Facebook Blue)
- Hotkey controls:
  - F6: Start/Pause the auto-clicker
  - F7: Exit the program
- Works in background
- Efficient color scanning
- Adjustable click delay

## Requirements
- Python 3.x
- Required packages:
  ```bash
  pip install pyautogui pillow pywin32 pynput
  ```
## Usage

1. Run the script
2. Move your mouse to the target area
3. Press F6 to start/pause the auto-clicker
4. Press F7 to exit the program

## Note

The auto-clicker scans a small area around the mouse cursor for the specified color and clicks automatically when detected.