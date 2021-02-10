import RPi.GPIO as GPIO
import time

Relay_Ch1 = 37
Relay_Ch2 = 40
Relay_Ch3 = 38
Relay_Ch4 = 35

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(Relay_Ch1,GPIO.OUT)
GPIO.setup(Relay_Ch2,GPIO.OUT)
GPIO.setup(Relay_Ch3,GPIO.OUT)
GPIO.setup(Relay_Ch4,GPIO.OUT)

def relay(pin):
    GPIO.output(pin,GPIO.LOW)
    print("Channel 1:The Common Contact is access to the Normal Open Contact!")
    time.sleep(0.5)
    GPIO.output(pin,GPIO.HIGH)
    print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
    time.sleep(0.5)
        

if __name__ == "__main__":
    i=1
    while i<3:
        relay(40)
        i+=1
    
    
        
    
