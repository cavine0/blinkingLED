import RPi.GPIO as GPIO
import time

button_pin = 17  
led_pin = 18    

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(led_pin, GPIO.OUT)

def button_pressed(channel):
    print("Button Pressed!")
    GPIO.output(led_pin, GPIO.HIGH) 

def button_released(channel):
    print("Button Released!")
    GPIO.output(led_pin, GPIO.LOW) 


GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_pressed, bouncetime=200)
GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_released, bouncetime=200)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program exited")
finally:
    GPIO.cleanup()