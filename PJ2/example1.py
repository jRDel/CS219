import RPi.GPIO as GPIO
import time
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

try:
    while True:
        GPIO.output(16, True)
        time.sleep(1)
        GPIO.output(16, False)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
    

