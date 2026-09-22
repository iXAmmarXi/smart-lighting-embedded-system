from signal import pause
from gpiozero import LED, Button, PWMLED
import time


SIGNAL = PWMLED(pin=18,initial_value=0)
#SIGNAL2 = Blinka(pin=18)

SIGNAL.value = 0.1
#SIGNAL.on()

#SIGNAL2.toggle(0.1)
# 
# time.sleep(2)
# SIGNAL.off()
# time.sleep(2)
# SIGNAL.on()
