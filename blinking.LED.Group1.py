import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
    blink_count = 0
    while True:
        # Turn the LED on
        GPIO.output(18, GPIO.HIGH)
        blink_count += 1
        print(f"Blink count: {blink_count}")
        time.sleep(1)  # Wait for 1 second
        
        # Turn the LED off
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()