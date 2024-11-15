import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the ultrasonic sensor
TRIG = 23  # Pin connected to TRIG
ECHO = 24  # Pin connected to ECHO

# Set up the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # Ensure the trigger pin is set low
    GPIO.output(TRIG, False)
    time.sleep(2)  # Give sensor time to settle
    
    # Send a 10us pulse to trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    # Wait for the echo to start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    
    # Wait for the echo to end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    
    # Calculate pulse duration
    pulse_duration = pulse_end - pulse_start
    
    # Calculate the distance (speed of sound is 330 m/s, divided by 2 for to and from distance)
    distance = pulse_duration * 33000 / 2  # Speed in cm/s
    
    return distance

try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()