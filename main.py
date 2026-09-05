import subprocess
import os
from signal import SIGSTOP, SIGCONT, SIGTERM
from pynput import keyboard

script = 'farm.py'
paused = False

process = subprocess.Popen(["python3", script])
pid = process.pid

def on_hotkey(key):
    global paused

    if key == keyboard.Key.f1:
        if paused:
            os.kill(pid, SIGCONT)
        else:
            os.kill(pid, SIGSTOP)
        paused = not paused

    if key == keyboard.Key.f2:
        os.kill(pid, SIGTERM)
        exit(0)

with keyboard.Listener(on_press=on_hotkey) as listener:
    listener.join()
