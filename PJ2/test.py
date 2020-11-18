import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

while True:
    if GPIO.input(12):
        print("Not pressed")
        time.sleep(1)
    else:
        print("Press")