#RelayTest.py - This script is intended to test the relays and make sure they are working.
#Aaron Ragusa - RagsFTW
#1-19-2019

import gpiozero
from time import sleep

relay1 = gpiozero.OutputDevice(26, active_high=False, initial_value=False)
relay3 = gpiozero.OutputDevice(20, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(21, active_high=False, initial_value=False)
relay4 = gpiozero.OutputDevice(19, active_high=False, initial_value=False)
relay5 = gpiozero.OutputDevice(16, active_high=False, initial_value=False)
relay6 = gpiozero.OutputDevice(13, active_high=False, initial_value=False)
relay7 = gpiozero.OutputDevice(6, active_high=False, initial_value=False)
relay8 = gpiozero.OutputDevice(5, active_high=False, initial_value=False)

i=1
while i<3:
    relay1.on()
    sleep (1)
    relay1.off()

    relay2.on()
    sleep(1)
    relay2.off()

    relay3.on()
    sleep(1)
    relay3.off()
    
    relay4.on()
    sleep (1)
    relay4.off()

    relay5.on()
    sleep(1)
    relay5.off()

    relay6.on()
    sleep(1)
    relay6.off()

    relay7.on()
    sleep(1)
    relay7.off()

    relay8.on()
    sleep(1)
    relay8.off()
    i+=1