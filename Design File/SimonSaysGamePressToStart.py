from random import choice
from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C  # Ensure the SSD1306_I2C library is installed

# Define the GPIO pins for each LED and corresponding buttons
led_pins = {
    "red": Pin(10, Pin.OUT),       # Red LED - GP10
    "green": Pin(11, Pin.OUT),     # Green LED - GP11
    "blue": Pin(18, Pin.OUT),      # Blue LED - GP18
    "purple": "purple",            # Purple LED - use the combination of red and blue components
    "purple_red": Pin(19, Pin.OUT), # Red component of Purple - GP19
    "purple_blue": Pin(17, Pin.OUT) # Blue component of Purple - GP17
}

button_pins = {
    "red": Pin(12, Pin.IN, Pin.PULL_DOWN),   # Button 1 for Red - GP12
    "green": Pin(13, Pin.IN, Pin.PULL_DOWN), # Button 2 for Green - GP13
    "blue": Pin(14, Pin.IN, Pin.PULL_DOWN),  # Button 3 for Blue - GP14
    "purple": Pin(15, Pin.IN, Pin.PULL_DOWN) # Button 4 for Purple - GP15
}

# Define the GPIO pin for the buzzer
buzzer = Pin(16, Pin.OUT)

# Initialize I2C and OLED display
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)  # Adjust pins for your setup
oled = SSD1306_I2C(128, 64, i2c)  # Create OLED object (128x64 resolution)

rnd_colors = []  # Random sequence
score = 0  # Initialize score

def play_buzzer(duration, frequency):
    """Play a tone on the buzzer."""
    period = 1 / frequency  # Period of the wave
    cycles = int(duration * frequency)  # Number of cycles
    for _ in range(cycles):
        buzzer.value(1)
        time.sleep(period / 2)  # High for half the period
        buzzer.value(0)
        time.sleep(period / 2)  # Low for half the period

def success_buzzer():
    """Play a success sound."""
    play_buzzer(0.2, 1000)  # High tone
    play_buzzer(0.2, 1200)  # Slightly higher tone

def failure_buzzer():
    """Play a failure sound."""
    play_buzzer(0.5, 300)  # Low tone
    time.sleep(0.2)
    play_buzzer(0.5, 300)  # Repeat the low tone

def flash_color(color, duration=0.5):
    if color == "purple":
        led_pins["purple_red"].value(1)
        led_pins["purple_blue"].value(1)
    else:
        led_pins[color].value(1)
    time.sleep(duration)
    if color == "purple":
        led_pins["purple_red"].value(0)
        led_pins["purple_blue"].value(0)
    else:
        led_pins[color].value(0)
    time.sleep(0.2)

def get_user_input():
    user_sequence = []
    for expected_color in rnd_colors:
        color_pressed = None
        while color_pressed is None:
            for color, button in button_pins.items():
                if button.value() == 1:
                    color_pressed = color
                    flash_color(color, 0.2)
                    time.sleep(0.3)  # Debounce delay
                    break
        user_sequence.append(color_pressed)
        if color_pressed != expected_color:
            return None
    return user_sequence

def update_display():
    oled.fill(0)  # Clear the display
    oled.text("Simon Says Game", 0, 0)  # Title at the top
    oled.text(f"Score: {score}", 0, 16)  # Display score
    oled.show()

# Start Screen: Wait for Button 1 (Red Button)
oled.fill(0)
oled.text("Simon Says Game", 0, 0)
oled.text("Press 1 to Start", 0, 16)
oled.show()

print("Waiting for Button 1 to Start...")
while button_pins["red"].value() == 0:
    time.sleep(0.1)  # Poll button state

# Main game loop
print("Game Starting!")
oled.fill(0)
oled.text("Simon Says Game", 0, 0)
oled.show()
time.sleep(2)

while True:
    rnd_colors.append(choice(["red", "green", "blue", "purple"]))
    print(f"Sequence so far: {rnd_colors}")

    for color in rnd_colors:
        flash_color(color)

    user_input = get_user_input()
    if user_input is None:
        failure_buzzer()  # Play failure sound
        oled.fill(0)
        oled.text("You lost!", 0, 0)
        oled.text(f"Final Score: {score}", 0, 16)
        oled.show()
        time.sleep(5)
        oled.fill(0)  # Turn off the display after 5 seconds
        oled.show()
        break

    score += 1
    success_buzzer()  # Play success sound
    update_display()
    print(f"Correct! Your current score is: {score}")
    time.sleep(1)
