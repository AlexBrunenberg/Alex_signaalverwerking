from gpiozero import LED
from signal import pause

red = LED(17)

red.blink(on_time=1,off_time=1,n=50,background=True)

pause()