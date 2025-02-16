import pyperclip
from pynput import keyboard

# List of words
words = [
# paste an array of words here. these words will be cycled through when you press v
]

index = 0

def on_press(key):
    global index

    try:
        if key.char == 'v':  # press v - > cycle next word
            pyperclip.copy(words[index])
            

            index = (index + 1) % len(words)

    except AttributeError:
        pass


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
