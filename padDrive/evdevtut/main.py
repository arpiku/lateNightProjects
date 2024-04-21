import evdev


##This is how one may print all the devices, all the devices are associated with a "file", it's not
# actually a "file" but *nix systems allow a device to be treated as a buffer from which things can
# be read or written to, open or closed, just like a file

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices: 
   print(device.path, device.name, device.phys) # another property is uniq


device = evdev.InputDevice('/dev/input/event20')
print(device)

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))



print(evdev.ecodes.KEY_A)
print(evdev.ecodes.ecodes['KEY_A'])
print(evdev.ecodes.KEY[30])
print(evdev.ecodes.bytype[ecodes.EV_KEY][30])
print(evdev.ecodes.KEY[152])
