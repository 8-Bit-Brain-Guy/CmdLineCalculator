import keyboard




keyboard.on_press(on_key_press)

def on_key_press(event):
    print("Taste gedrückt: ", event.name)
    print("Scan code:      ", event.scan_code)
    print("Timestamp:      ", event.time)

# Halten Sie das Programm am Laufen, damit es Tastatureingaben abfragen kann
keyboard.wait('esc')


