from machine import Pin
import time

# Configure GPIO pins for the LEDs
led_pins = [10, 11, 18]  # Pins for Red, Green, Blue LEDs
yellow_pins = [17, 19]   # Two pins for Yellow LED (AND logic)
leds = [Pin(pin, Pin.OUT) for pin in led_pins]
yellow_leds = [Pin(pin, Pin.OUT) for pin in yellow_pins]

def set_yellow(state):
    """Control the Yellow LED (requires both pins to be HIGH)."""
    for pin in yellow_leds:
        pin.value(state)

def flash_leds():
    try:
        while True:
            # Flash Red, Green, Blue LEDs
            for led in leds:
                led.on()          # Turn LED on
                time.sleep(0.2)   # Wait 200ms
                led.off()         # Turn LED off

            # Flash Yellow LED (requires both pins to be HIGH)
            print("Turning on Yellow LED")
            set_yellow(1)         # Turn on Yellow LED (both pins HIGH)
            time.sleep(0.2)       # Wait 200ms
            set_yellow(0)         # Turn off Yellow LED (both pins LOW)
            time.sleep(0.5)       # Wait 500ms before the next cycle

    except KeyboardInterrupt:
        print("Exiting program.")
    finally:
        # Ensure all LEDs are turned off
        for led in leds:
            led.off()
        set_yellow(0)  # Turn off Yellow LED
        print("All LEDs are off.")

# Run the flashing sequence
flash_leds()
