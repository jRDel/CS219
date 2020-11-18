import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

time.sleep(3) #gives time to press button to start
if GPIO.input(25):
    print("Button not pressed. Exiting")
else:
    while True:
        if GPIO.input(25):
            GPIO.output(18, True)
            time.sleep(1)
            GPIO.output(18, False)
            time.sleep(1)
            input2 = GPIO.input(25)
            if input2:
                continue
            else:
                break
            
            

    

                
    
    
    
    
    
    
    


