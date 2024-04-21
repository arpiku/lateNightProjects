import math
import time
import pyautogui

# Define the radius and center of the circle
radius = 100
center_x, center_y = pyautogui.size()  # Get screen resolution and use it as center coordinates

# Calculate the angle step for each movement
angle_step = math.pi / 180  # 1 degree in radians

# Move the cursor in a circle
for angle in range(0, 361):  # Loop through 0 to 360 degrees
    x = center_x + int(radius * math.cos(angle * angle_step))
    y = center_y + int(radius * math.sin(angle * angle_step))
    pyautogui.moveTo(x, y, duration=0.01)  # Move to the calculated position
    time.sleep(0.01)  # Pause for a short duration for smooth movement
