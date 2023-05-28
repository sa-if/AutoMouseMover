import pyautogui
import random
import time

# Set the minimum and maximum speed of the mouse movement
min_speed = 100
max_speed = 300

# Set the minimum and maximum time between movements
min_wait = 0.5
max_wait = 3.0

# Get the size of the screen
screen_width, screen_height = pyautogui.size()

# Move the mouse cursor randomly with more human-like movement
while True:
    # Generate a random point on the screen
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    # Generate a random speed for the mouse movement
    speed = random.uniform(min_speed, max_speed)

    # Move the mouse cursor to the random point with the random speed
    pyautogui.moveTo(x, y, duration=speed/1000)

    # Generate a random time to wait before the next movement
    wait_time = random.uniform(min_wait, max_wait)

    # Wait for the random amount of time
    time.sleep(wait_time)
