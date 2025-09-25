from gpiozero import LEDBoard # importeer LEDBoard
from time import sleep  # importeer sleep

leds = LEDBoard(4,17,27,22,10,9,5,6)    # gebruik de functie LEDBoard en zet er pinnen in van leds

richting = 0 # maak variabele richting aan
led = 0 # maak variabele led aan

while True: # doe de hele tijd
    if led == 0:    # als led 0 is
        richting = 0    # maak richting gelijk aan 0
    elif led == 7:  # anders als led 7 is
        richting = 1    # maak richting gelijk aan 1
    leds[led].on()  # maak index led van leds hoog 
    sleep(0.1)  # wacht 100ms
    leds[led].off() # maak index led van leds laag
    if richting == 0:   # als richting gelijk is aan 0
        led += 1    # doe 1 bij led
    else:   # anders
        led = led - 1 # doe 1 van led af