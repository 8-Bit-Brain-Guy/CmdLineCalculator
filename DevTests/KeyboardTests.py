import keyboard

value = None


def on_key_press(event):
    print("Taste gedrückt: ", event.name)
    print("Scan code:      ", event.scan_code)
    print("Timestamp:      ", event.time)
    ## if event.name == 'esc':
    ##    keyboard.unhook_all()
    value = event.scan_code


keyboard.on_press(on_key_press)

# Halten Sie das Programm am Laufen, damit es Tastatureingaben abfragen kann
keyboard.wait('esc')
print(value)
## while True:
##     if keyboard.is_pressed("q"):
##         print("QQQQ")

