import evdev
from selectors import DefaultSelector, EVENT_READ

ecodes = evdev.ecodes

is_button_pressed = False
last_x = 0
last_y = 0


selector = DefaultSelector()

padInputs = [evdev.InputDevice(path) for path in evdev.list_devices() if evdev.InputDevice(path).uniq == "C6T12SH00001"]

print(padInputs)

caps = [input.capabilities(verbose=True) for input in padInputs]

for cap in caps:
   print(cap)

# padInputs[0].grab()
# padInputs[1].grab()
# padInputs[2].grab()

selector.register(padInputs[0],EVENT_READ) #MOUSE (for the wheel)
selector.register(padInputs[1],EVENT_READ) #Keyboard and wheel
selector.register(padInputs[2],EVENT_READ) #PEN 


ui = evdev.UInput()

