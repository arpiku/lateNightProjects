import pyautogui as pg

from utils import *
from evdev import ecodes as e, list_devices, AbsInfo, InputDevice, UInput

import math
import time
from pywayland.client import Display
from pywayland.protocol.wayland import WlOutput

from typing import List

def move_mouse():
    print(pg.size())
    while True:
        print(pg.position())

def move_mouse_wayland():
    display = Display()
    registry = display.get_registry()

    screen_width = 0
    screen_height = 0

    def handle_global(name, interface, version):
        global screen_width, screen_height
        if interface == 'wl_output':
            output = registry.bind(name, WlOutput, version)
            screen_width = output.get_width()
            screen_height = output.get_height()

    registry.set_global_handler(handle_global)

    display.dispatch()
    display.roundtrip()

    print(f"Screen width: {screen_width}, Screen height: {screen_height}")

    radius = min(screen_width, screen_height) // 4  # Use quarter of the smaller dimension as radius

    for angle in range(0, 361):  # Loop through 0 to 360 degrees
        x = screen_width // 2 + int(radius * math.cos(angle * math.pi / 180))
        y = screen_height // 2 + int(radius * math.sin(angle * math.pi / 180))
        print(f"Moving mouse to: ({x}, {y})")  # Print the position (for demonstration)
        time.sleep(0.01)  # Pause for a short duration for smooth movement

    display.disconnect()


def inject_events(devices):
    print("Listening for events (press ctrl-c to exit) ...")
    fd_to_device = {dev.fd: dev for dev in devices}
    while True:
        r, w, e = select.select(fd_to_device, [], [])
        for fd in r:
            for event in fd_to_device[fd].read():
                print_event(event)

def main():
    move_mouse_wayland()
    pass


        




if __name__ == "__main__":

    # device_test(grab_devices=True,print_capabilities_of_dev=True)
    main()
