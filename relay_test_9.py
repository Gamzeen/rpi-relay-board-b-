import RPi.GPIO as GPIO
import time 
Relay_channel = [11, 12]
GPIO.setwarnings(False)

def relay_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Relay_channel[0], GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(Relay_channel[1], GPIO.OUT, initial=GPIO.HIGH)
    time.sleep(2)
def relay(Relay):  
    print ('...Relay channel %d on' % (Relay))
    GPIO.output(Relay_channel[Relay], GPIO.LOW)
    time.sleep(0.5)
    print ('...Relay channel %d off' % (Relay))
    GPIO.output(Relay_channel[Relay], GPIO.HIGH)
    time.sleep(0.5)
    

if __name__ == '__main__':
    relay_setup()
    i=1
    while i<3:
        relay(0)
        relay(1)
        i+=1