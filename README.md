# Color Detection Auto-Clicker

A Python auto-clicker that automatically clicks when it detects a specific color (#0866FF) under the mouse cursor.

## Features

- Color detection (#0866FF - Facebook Blue)
- Smart clicking:
  - Only clicks when the "Poke" button is blue (active)
  - Skips when button is grey (inactive/poked)
- Hotkey controls:
  - F6: Start/Pause the auto-clicker
  - F7: Exit the program
- Works in background
- Efficient color scanning
- Adjustable click delay

## Button States

The auto-clicker detects these states:

Inactive (Grey) - Will not click:  
![Poked Button](images/poked_button.png)

Active (Blue) - Will click:  
![Poke Button](images/poke_button.png)

## Requirements
- Python 3.x
- Required packages:
  ```bash
  pip install pyautogui pillow pywin32 pynput
  ```

## Usage
1. Run the script
2. Move your mouse over the "Poke" button area
3. Press F6 to start/pause the auto-clicker
4. The script will automatically:
   - Click when the button is blue (#0866FF)
   - Skip when the button is grey (already poked)
5. Press F7 to exit the program

## Note
The auto-clicker scans a small area around the mouse cursor and only clicks when it detects the active blue Poke button color (#0866FF). It will not click on grey or inactive buttons.
